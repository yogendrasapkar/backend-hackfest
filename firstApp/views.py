from django.shortcuts import render
from django.http import HttpResponse
from django.http.response import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout

#for apis
from .serializers import medicalsummarySerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import medicalsummary

# Create your views here.
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

class medicalsummaryView(APIView):
    def get(self, request):
        player1 = medicalsummary.objects.all()
        serialize = medicalsummarySerializer(player1, many=True)
        return Response(serialize.data)
    
    def post(self, request):
        serialize = medicalsummarySerializer(data=request.data)
        if(serialize.is_valid()):
            serialize.save()
            return Response(serialize.data)
        return Response(serialize.errors)