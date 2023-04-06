from django.contrib import admin

# Register your models here.
from userinter.models import ContactForm
class service(admin.ModelAdmin):
    jack=("firstname","lastname","email","subject")
admin.site.register(ContactForm,service)