from rest_framework import serializers
from .models import medicalsummary,problemList ,dignosticsresults ,pasthistory

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
