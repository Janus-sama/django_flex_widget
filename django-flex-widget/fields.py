from django import forms

from .widgets import DurationInput
from .widgets import DynamicTextWidget


class DynamicTextField(forms.CharField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("widget", DynamicTextWidget)
        super().__init__(*args, **kwargs)

    def to_python(self, value):
        if not value:
            return ""
        if isinstance(value, list):
            return ";".join(value)
        return value

    def validate(self, value):
        if not value:
            return
        if not isinstance(value, str):
            raise forms.ValidationError(
                self.error_messages["invalid"], code="invalid")
        super().validate(value)
        

class DurationField(forms.DurationField):
    widget = DurationInput

    def to_python(self, value: str):
        if value:
            days, unit = value.split("_")
            if unit == "days":
                return timedelta(days=int(days))
            if unit == "weeks":
                return timedelta(weeks=int(days))
            if unit == "months":
                return timedelta(days=int(days) * 30)
        return None
