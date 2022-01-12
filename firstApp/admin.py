from django.contrib import admin
from .models import medicalsummary, prescription

# Register your models here.
admin.site.register(medicalsummary)

admin.site.register(prescription)