from rest_framework import serializers
from .models import medicalsummary,problemList

class medicalsummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = medicalsummary
        #fields = {'fname','lname'}
        fields = '__all__'

class problemListSerializer(serializers.ModelSerializer):
    class Meta:
        model = problemList
        fields = '__all__'
