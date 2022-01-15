from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import medicalsummary, prescription,patientInfo,planCare,dignosticsresults

# Register your models here.
admin.site.register(medicalsummary)

admin.site.register(prescription)
admin.site.register(patientInfo)
admin.site.register(planCare)
admin.site.register(dignosticsresults)