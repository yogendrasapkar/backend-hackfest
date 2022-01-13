from django.db.models import fields
from rest_framework import serializers
from .models import medicalsummary,problemList ,dignosticsresults ,pasthistory, planCare, prescription
from django.contrib.auth.models import User

class userSerializers(serializers.ModelSerializer):
 
    class Meta:
        model = User
        fields =  '__all__'

class medicalsummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = medicalsummary
        #fields = {'fname','lname'}
        fields = '__all__'

class problemListSerializer(serializers.ModelSerializer):
    class Meta:
        model = problemList
        fields = '__all__'

# create dignostics-result
class dignosticsresultSerializer(serializers.ModelSerializer):
    class Meta:
        model = dignosticsresults
        #fields = {'fname','lname'}
        fields = '__all__'

# Create past_History_Of_illnesses 
class pasthistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = pasthistory
        #fields = {'fname','lname'}
        fields = '__all__'


class planCareSerializer(serializers.ModelSerializer):
    class Meta:
        model = planCare
        fields = '__all__'


# create prescription
class prescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = prescription
        fields = '__all__'