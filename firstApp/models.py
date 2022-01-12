from django.db import models

# Create your models here.
class medicalsummary(models.Model):
    medication_item = models.CharField(max_length=50)
    form = models.CharField(max_length=50)
    strength_concentration = models.FloatField()
    presentation = models.CharField(max_length=50)
    manufacturer = models.CharField(max_length=50)
    expire = models.DateField()
    batch_id_timing = models.CharField(max_length=50)
    amount = models.FloatField()
    amount_unit = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    patient_id = models.IntegerField()

    def __str__(self):
        return self.form


class problemList(models.Model):
    diagnosisName = models.CharField(max_length=100)
    bodySite = models.CharField(max_length=100)
    dateOfOnset = models.DateField()
    severity = models.CharField(max_length=100)
    diagnosticCertainity = models.CharField(max_length=100)
    patient_id = models.IntegerField()

    def __str__(self):
        return self.diagnosisName


# create Diagnostics-result model
class dignosticsresults(models.Model):
    test_name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    test_result = models.CharField(max_length=50)
    patient_id = models.IntegerField()

    def __str__(self):
        return self.patient_id


# create Past History of illnesses model
class pasthistory(models.Model):
    diagnosis_name = models.CharField(max_length=50)
    body_site = models.CharField(max_length=100)
    date_of_onsite = models.DateField()
    severity = models.CharField(max_length=100)
    Problem_Qualifier = models.CharField(max_length=100)
    diagnostic_certainty = models.CharField(max_length=100)
    patient_id = models.IntegerField()

    def __str__(self):
        return self.patient_id