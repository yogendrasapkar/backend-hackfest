from rest_framework import serializers
from .models import medicalsummary,dignosticsresult

class medicalsummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = medicalsummary
        #fields = {'fname','lname'}
        fields = '__all__'

# create dignostics-result
class dignosticsresultSerializer(serializers.ModelSerializer):
    class Meta:
        model = dignosticsresult
        #fields = {'fname','lname'}
        fields = '__all__'