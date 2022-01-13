from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import medicalsummary, prescription

# Register your models here.
admin.site.register(medicalsummary)

admin.site.register(prescription)