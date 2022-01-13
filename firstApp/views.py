from django.shortcuts import render
from django.http import HttpResponse
from django.http.response import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from rest_framework import serializers
from rest_framework.serializers import Serializer

#for apis
from .serializers import medicalsummarySerializer,problemListSerializer,dignosticsresultSerializer,pasthistorySerializer, planCareSerializer, prescriptionSerializer
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import medicalsummary,problemList ,dignosticsresults,pasthistory, planCare, prescription
from rest_framework import viewsets
from .serializers import userSerializers
from django.contrib.auth.models import User

# Create your views here.
class userviewsets(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = userSerializers

def index(request):
    return render(request, 'index.html')

def register(request):
    if request.method == "POST":
        f = UserCreationForm(request.POST)
        if f.is_valid():
            f.save()
    else:
        f = UserCreationForm()
    return render(request, "register.html", {"form": f})


# def signin(request):
#     if request.method == "POST":
#         url = request.get('api-token-auth/ username="Himach" password="Hello@123"')
#         print(url)
#         return HttpResponseRedirect('/home')
        # f = AuthenticationForm(request=request, data=request.POST)
        # if f.is_valid():
        #     un = f.cleaned_data['username']
        #     pd = f.cleaned_data['password']
        #     user = authenticate(username = un, password = pd)
        #     if user is not None:
        #         login(request,user)
        #         return HttpResponseRedirect('/home')

def signin(request):
    if request.method == "POST":
        f = AuthenticationForm(request=request, data=request.POST)
        if f.is_valid():
            un = f.cleaned_data['username']
            pd = f.cleaned_data['password']
            user = authenticate(username = un, password = pd)
            if user is not None:
                login(request,user)
                return HttpResponseRedirect('/home')
    else:
        f = AuthenticationForm()
    return render(request, 'signin.html', {'form': f})

def home(request):
    return render(request, 'home.html',  {'name': request.user})

def userLogout(request):
    logout(request)
    return HttpResponseRedirect('/signin')


# Medical summary api's
# Get all the records
@api_view(['GET'])
def getAllMedicalSummary(request):
    if request.method == 'GET':
        medicalRecord = medicalsummary.objects.all()
        serialize = medicalsummarySerializer(medicalRecord, many=True)
        return Response(serialize.data)

# Get only one record based on id
@api_view(['GET'])
def getOneMedicalSummary(request, pk):
    if request.method == 'GET':
        medicalRecord = medicalsummary.objects.get(id=pk)
        serialize = medicalsummarySerializer(medicalRecord, many=False)
        return Response(serialize.data)

# Add one record
@api_view(['POST'])
def addOneRecord(request):
    if request.method == 'POST':
        serialize = medicalsummarySerializer(data=request.data)
        if(serialize.is_valid()):
            serialize.save()
            return Response(serialize.data)
        return Response(serialize.errors)

# Update a record based on id
@api_view(['POST'])
def updateRecord(request, pk):
    if request.method == 'POST':
        medicalRecord = medicalsummary.objects.get(id=pk)
        serialize = medicalsummarySerializer(instance=medicalRecord, data=request.data)
        if(serialize.is_valid()):
            serialize.save()
            return Response(serialize.data)

# Delete a record
@api_view(['DELETE'])
def deleteRecord(request, pk):
    if request.method == 'DELETE':
        medicalRecord = medicalsummary.objects.get(id=pk)
        medicalRecord.delete()
        return Response("Record deleted successfully")

# class medicalsummaryView(APIView):
#     def get(self, request):
#         player1 = medicalsummary.objects.all()
#         serialize = medicalsummarySerializer(player1, many=True)
#         return Response(serialize.data)

#     def get(self, request, pk, format=None):
#         player1 = medicalsummary.objects.get(id=pk)
#         serialize = medicalsummarySerializer(player1, many=False)
#         return Response(serialize.data)
    
#     def post(self, request):
#         serialize = medicalsummarySerializer(data=request.data)
#         if(serialize.is_valid()):
#             serialize.save()
#             return Response(serialize.data)
#         return Response(serialize.errors)


# problemList apis
# get all records from problem list
@api_view(['GET'])
def getProblemList(request):
    if request.method=="GET":
        probListRecord = problemList.objects.all()
        serialize = problemListSerializer(probListRecord, many=True)
        return Response(serialize.data)


# get a record from problem list based on specific id
@api_view(['GET'])
def getOneProblemList(request,pk):
    if request.method == "GET":
        probListRecord = problemList.objects.get(id=pk)
        serialize= problemListSerializer(probListRecord, many=False)
        return Response(serialize.data)

# add a record in problem list
@api_view(['POST'])
def addOneToProblemList(request):
    if request.method=="POST":
        serialize = problemListSerializer(data=request.data)
        if(serialize.is_valid()):
            serialize.save()
            return Response(serialize.data)
        return Response(serialize.errors)

# update a record in problem list based on specific id
@api_view(['POST'])
def updateProblemList(request,pk):
    if request.method=="POST":
        probListRecord = problemList.objects.get(id=pk) 
        serialize = problemListSerializer(instance=probListRecord,data=request.data)
        if(serialize.is_valid()):
            serialize.save()
            return Response(serialize.data)

# delete a record from problem list based on specific id
@api_view(['DELETE'])
def deleteProblemList(request,pk):
    if request.method=="DELETE":
        probListRecord = problemList.objects.get(id=pk)
        probListRecord.delete()
        return Response("Record deleted from Problem List")



# diagnostics-result api
# view all diagnostics records
@api_view(['GET'])
def getAllDiagnosticResults(request):
    if request.method == 'GET':
        diagnosticRecord =dignosticsresults.objects.all()
        serialize = dignosticsresultSerializer(diagnosticRecord, many=True)
        return Response(serialize.data)

#view one diagnostic records
@api_view(['GET'])
def getOneDiagnosticResults(request,pk):
    if request.method == 'GET':
        diagnosticRecord =dignosticsresults.objects.get(id=pk)
        serialize = dignosticsresultSerializer(diagnosticRecord, many=False)
        return Response(serialize.data)

# Add one diagnostic-result 
@api_view(['POST'])
def addOneDiagnosticRecord(request):
    if request.method == 'POST':
        serialize = dignosticsresultSerializer(data=request.data)
        if(serialize.is_valid()):
            serialize.save()
            return Response(serialize.data)
        return Response(serialize.errors)

# Update Diagnostic result record
@api_view(['POST'])
def updateDiagnosticRecord(request, pk):
    if request.method == 'POST':
        diagnosticRecord = dignosticsresults.objects.get(id=pk)
        serialize = dignosticsresultSerializer(instance= diagnosticRecord , data=request.data)
        if(serialize.is_valid()):
            serialize.save()
            return Response(serialize.data)


# Delete a Diagnostic Result record
@api_view(['DELETE'])
def deleteDiagnosticRecord(request, pk):
    if request.method == 'DELETE':
        dignosticRecord = dignosticsresults.objects.get(id=pk)
        dignosticRecord.delete()
        return Response(" Dignostics Result Record deleted successfully")


# Past_History_of_illness api

# View all Patient Past_history_illnesses 
@api_view(['GET'])
def getAllPastHistoryIllnessResult(request):
    if request.method == 'GET':
        pastRecord =pasthistory.objects.all()
        serialize = pasthistorySerializer(pastRecord, many=True)
        return Response(serialize.data)

#view one  Patient Past_history_illnesses record
@api_view(['GET'])
def getOnePastHistoryResults(request,pk):
    if request.method == 'GET':
        pastRecord =pasthistory.objects.get(id=pk)
        serialize = pasthistorySerializer(pastRecord, many=False)
        return Response(serialize.data)

# Add one Patient Past_history_illnesses record
@api_view(['POST'])
def addOneIllnessRecord(request):
    if request.method == 'POST':
        serialize = pasthistorySerializer(data=request.data)
        if(serialize.is_valid()):
            serialize.save()
            return Response(serialize.data)
        return Response(serialize.errors)


# Update Patient Past_history_illnesses record
@api_view(['POST'])
def updateIllnessRecord(request, pk):
    if request.method == 'POST':
        pastRecord = pasthistory.objects.get(id=pk)
        serialize = pasthistorySerializer(instance= pastRecord , data=request.data)
        if(serialize.is_valid()):
            serialize.save()
            return Response(serialize.data)


# Delete a Patient Past_history_illnesses record
@api_view(['DELETE'])
def deleteIllnessRecord(request, pk):
    if request.method == 'DELETE':
        pastRecord = pasthistory.objects.get(id=pk)
        pastRecord.delete()
        return Response(" Past History Illness Record deleted successfully")



# Plan care apis
# get all records from plan care
@api_view(['GET'])
def getPlanCare(request):
    if request.method=="GET":
        planCareRecord=planCare.objects.all()
        serialize = planCareSerializer(planCareRecord,many=True)
        return Response(serialize.data)

# get a record from plan care based on specific id
@api_view(['GET'])
def getOnePlanCare(request,pk):
    if request.method == "GET":
        planCareRecord = planCare.objects.get(id=pk)
        serialize = planCareSerializer(planCareRecord,many=False)
        return Response(serialize.data)

# add a record to plan care
@api_view(['POST'])
def addOneToPlanCare(request):
    if request.method == "POST":
        serialize = planCareSerializer(data=request.data)
        if(serialize.is_valid()):
            serialize.save()
            return Response(serialize.data)
        return Response(serialize.errors)

# update a record in plan care based on specific id
@api_view(['POST'])
def updatePlanCare(request,pk):
    if request.method == "POST":
        planCareRecord = planCare.objects.get(id=pk)
        serialize = planCareSerializer(instance=planCareRecord,data=request.data)
        if(serialize.is_valid()):
            serialize.save()
            return Response(serialize.data)

# delete a record from plan care based on specific id
@api_view(['DELETE'])
def deletePlanCare(request,pk):
    if request.method == 'DELETE':
        planCareRecord = planCare.objects.get(id=pk)
        planCareRecord.delete()
        return Response("The record has been deleted")


# Prescription apis
# get all records of a patient from prescription
@api_view(['GET'])
def getPrescription(request,fk):
    if request.method=="GET":
        prescriptionRecord = prescription.objects.filter(patient_id=fk)
        serialize = prescriptionSerializer(prescriptionRecord,many=True)
        return Response(serialize.data)

# get one record from prescription
@api_view(['GET'])
def getOnePrescription(request,pk):
    if request.method == "GET":
        prescriptionRecord = prescription.objects.get(id=pk)
        serialize = prescriptionSerializer(prescriptionRecord,many=False)
        return Response(serialize.data)

# add a record to prescription
@api_view(['POST'])
def addOnePrescription(request):
    if request.method == "POST":
        serialize = prescriptionSerializer(data=request.data)
        if(serialize.is_valid()):
            serialize.save()
            return Response(serialize.data)
        return Response(serialize.errors)

# update a record in prescription based on specific id
@api_view(['POST'])
def updatePrescription(request,pk):
    if request.method == "POST":
        prescriptionRecord = prescription.objects.get(id=pk)
        serialize = prescriptionSerializer(instance=prescriptionRecord,data=request.data)
        if(serialize.is_valid()):
            serialize.save()
            return Response(serialize.data)