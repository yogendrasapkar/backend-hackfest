from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import medicalsummary, prescription,patientInfo

# Register your models here.
admin.site.register(medicalsummary)

admin.site.register(prescription)
admin.site.register(patientInfo)