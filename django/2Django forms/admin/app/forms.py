from django.db import models
from django import forms
from .models import table
class login(forms.Form):
    fname=forms.CharField(max_length=50)
    lname=forms.CharField(max_length=50)
    email=forms.EmailField()
    password=forms.CharField(widget=forms.PasswordInput())
    
class CarryData(forms.ModelForm):
    class Meta:
        model=table
        fields=('fname','lname','email','password')