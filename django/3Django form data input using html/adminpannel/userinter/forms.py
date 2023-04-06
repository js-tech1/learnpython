from django import forms
from .models import ContactForm

class FormContactForm(forms.ModelForm):
    class Meta:
        model= ContactForm
        fields= ["firstname","lastname","email","subject"]