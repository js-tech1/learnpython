from django.db import models

# Create your models here.
class ContactForm(models.Model):
    firstname= models.CharField(max_length=100)
    lastname= models.CharField(max_length=50)
    email= models.EmailField()
    subject= models.CharField(max_length=200)