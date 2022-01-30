from django.contrib import admin

# Register your models here.
from .models import Patient, Task

admin.site.register(Patient)
admin.site.register(Task)
