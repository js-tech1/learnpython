from django.contrib import admin
from .models import table
# Register your models here.
class submit(admin.ModelAdmin):
    varible=("fname","lname","email","roll_number","password")
admin.site.register(table,submit)
