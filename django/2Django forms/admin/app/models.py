from django.db import models

# Create your models here.
from django import forms

class table(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=50)