# DJANGI FLEX WIDGET (it took me a while to think of that name)
Custom Duration and Dynamic Text Fields for Django Forms
This project provides two custom fields and widgets for Django forms: a `DurationField` with a `DurationInput` widget and a `DynamicTextField` with a `DynamicTextWidget`. These fields allow for customizable form inputs, making it easier to handle duration values and dynamic multi-text inputs. 

More custom widgets will be added when I have time :D

## Features
- **Duration Field:** Customizable duration input with support for days, weeks, months, and years.
- **Dynamic Text Field:** A text field that dynamically generates multiple text inputs in the same field.
- Easy integration into existing Django forms with minimal setup.
- Custom validation for both duration and dynamic text values.
- Optionally supports django-crispy-forms and django-bootstrap5 for better styling.

## Installation
This project requires Django 3.0+. To install, simply download or clone the repository into your Django project.
```
git clone https://github.com/Janus-sama/django-duration-and-dynamic-fields.git
```
Or manually download the files and include them in your project.

Optional Dependencies
For better styling of your forms, you can use:
1. django-crispy-forms
2. django-bootstrap5
You can install these with:

```
pip install django-crispy-forms django-bootstrap5
```
Then configure crispy-forms in your settings:

```
INSTALLED_APPS = [
    'crispy_forms',
    'crispy_bootstrap5',
    # Your other apps
]

CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"
```

## Usage
**1. Duration Field**
1. Add the following import to your forms:
```
from .widgets import DurationField
```
2. Use the custom field in your Django form:
```
class MyForm(forms.Form):
    duration = DurationField(label="Duration")
```
3. The widget will appear in your form, allowing users to specify a time duration with units (days, weeks, months, years).
   
**2. Dynamic Text Field**
   1. Add the following import to your forms:
      ```
      from .widgets import DynamicTextField
      ```
   2. Use the custom dynamic text field in your Django form:
```
class MyForm(forms.Form):
    dynamic_text = DynamicTextField(label="Dynamic Text")
```
This field allows users to dynamically add multiple text inputs, which will be stored as a single string with each entry separated by a semicolon (;).

## Example
```
from django import forms
from .widgets import DurationField, DynamicTextField

class TaskForm(forms.Form):
    task_name = forms.CharField(label="Task Name", max_length=100)
    task_duration = DurationField(label="Task Duration")
    task_notes = DynamicTextField(label="Task Notes")
```
## Customization
**1. Duration Field**
You can customize the widget appearance by modifying the unit_choices during initialization. This allows you to restrict the available units.

### Example:
```
duration = DurationField(
    label="Custom Duration",
    widget=DurationInput(unit_choices=[
        ("days", "Days"),
        ("weeks", "Weeks"),
    ])
)
```
**2. Dynamic Text Field**
You can customize the DynamicTextField widget by specifying the text for the "Add" button during initialization.

### Example:
```
dynamic_text = DynamicTextField(
    label="Custom Dynamic Text",
    widget=DynamicTextWidget(add_text_button_text="Add More Text")
)
```

## Templates
The corresponding HTML templates for these custom widgets are included in the widgets/ directory.
`dynamic_text_widget.html`
`duration.html`
