from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from rest_framework import viewsets
from .serialzers import *
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

class patientsdata(viewsets.ModelViewSet):
    queryset=patient.objects.all()
    serializer_class=PatientSerializers
 