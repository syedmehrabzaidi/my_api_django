from django.shortcuts import render
from rest_framework import viewsets
from .serializers import StudentSerializers 
from .models import students

# Create your views here.
class StudentsViewSet(viewsets.ModelViewSet):
    queryset =students.objects.all().order_by('firstname')
    serializer_class = StudentSerializers