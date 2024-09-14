from datetime import timedelta

from django import forms
from django.core.exceptions import ValidationError
from django.forms.widgets import TextInput
from django.utils.translation import gettext_lazy as _


class DurationInput(forms.MultiWidget):
    template_name = "widgets/duration.html"

    def __init__(self, attrs=None, unit_choices=None):
        self.unit_choices = unit_choices or [
            ("days", _("Days")),
            ("weeks", _("Weeks")),
            ("months", _("Months")),
            ("years", _("Years")),
        ]
        attrs = attrs or {}

        widgets = (
            forms.TextInput(attrs=attrs),
            forms.Select(choices=self.unit_choices, attrs=attrs),
        )
        super().__init__(widgets, attrs)

    def decompress(self, value):
        if value:
            try:
                days, unit = value.split("_")
                days = int(days)
                if days < 0:
                    raise ValidationError(_("Duration cannot be negative."))
                return [str(days), unit]
            except (ValueError, ValidationError):
                return [None, None]
        return [None, None]

    def format_output(self, rendered_widgets):
        return "".join(rendered_widgets)

    def value_from_datadict(self, data, files, name):
        print("DATA: ", data)
        days = data.get(name + "_0")
        unit = data.get(name + "_1")

        if days is None and unit is None:
            return None
        if days is None or unit is None:
            raise ValidationError(
                _("Please provide both days and unit for the duration."))
        try:
            days = int(days)
        except ValueError:
            raise ValueError from ValidationError(
                _("Days must be an integer."))
        if days < 0:
            raise ValidationError(_("Duration cannot be negative."))
        if unit not in [c[0] for c in self.unit_choices]:
            raise ValidationError(_("Invalid unit for the duration."))

        return f"{days}_{unit}"

    def formatted_timedelta(self, value: str):

        if value:
            to_int = value.rsplit()[0]

            value = timedelta(days=int(to_int))
            # Convert duration to weeks and days
            weeks = value.days // 7
            days = value.days % 7

            data = {}

            # Logic to display the duration of the next visit
            if weeks >= 52:
                data["unit"] = "years"
                data["days"] = f"{weeks // 52}"
                return data
            if weeks >= 4:
                data["unit"] = "months"
                data["days"] = f"{weeks//4}"
                return data
            if weeks > 0:
                data["unit"] = "weeks"
                data["days"] = f"{weeks}"
                return data
            if days > 0:
                data["unit"] = "days"
                data["days"] = f"{days}"
                return data

        return None

    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)
        context["widget"]["unit_choices"] = self.unit_choices
        context["name"] = name
        context["id"] = attrs.get("id")

        if value:
            value = self.formatted_timedelta(value)
            context["widget"]["value"] = value
        context["widget"]["attrs"] = attrs

        return context


class DynamicTextWidget(TextInput):
    template_name = "widgets/dynamic_text_widget.html"

    def __init__(self, attrs=None, *args, **kwargs):
        attrs = attrs or {}
        self.add_text_button_text = kwargs.pop("add_text_button_text", "Add")
        super().__init__(attrs, *args, **kwargs)

    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)
        context["widget"]["add_text_button_text"] = self.add_text_button_text
        context["name"] = name

        context["widget"]["attrs"]["class"] = " ".join(
            [*attrs.get("class", []), "form-control"])

        # Set id attribute dynamically
        context["widget"]["attrs"]["id"] = attrs.get("id")
        context["widget"]["attrs"]["spellcheck"] = attrs.get(
            "spellcheck", True)

        # Ensure value is a list
        value = value if value else [""] * 4
        if not isinstance(value, list):
            value = value.split(";")

        context["widget"]["value"] = value

        return context

    def value_from_datadict(self, data, files, name):
        value = data.getlist(name)
        if value and isinstance(value, str):
            value = value.split(";")
        return value if value else [""] * 4


