# ecc/forms.py
from django import forms
from .models import ECCInput

class ECCInputForm(forms.ModelForm):
    class Meta:
        model = ECCInput
        fields = ['option', 'a', 'b', 'p', 'x', 'y', 'curve_type']

    def __init__(self, *args, **kwargs):
        super(ECCInputForm, self).__init__(*args, **kwargs)

        # Set required attribute to False for all fields
        for field_name, field in self.fields.items():
            field.required = False


