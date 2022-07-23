from django.shortcuts import render
from rest_framework import viewsets
from .serializers import EmployeeSerializer
from .models import Employee
#from . models import DRFPost
from rest_framework import permissions

class EmployeeViewSet(viewsets.ModelViewSet):
      queryset = Employee.objects.all()
      serializer_class = EmployeeSerializer
      permission_classes = [permissions.IsAuthenticated]
# Create your views here.'''
