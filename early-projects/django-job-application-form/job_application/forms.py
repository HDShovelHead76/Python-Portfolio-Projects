from django import forms
from .models import Form   # make sure this matches your actual model name

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Form
        fields = ["first_name", "middle_name", "last_name", "email", "phone", "occupation"]
        widgets = {
            "occupation": forms.RadioSelect,
        }
