from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import mixins

from .serializers import carreraSerializer
from .models import Carrera

# Create your views here.
class carreraView (viewsets.ModelViewSet):
    serializer_class = carreraSerializer
    queryset = Carrera.objects.all()
