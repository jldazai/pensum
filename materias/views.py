from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import mixins
from ast import Raise
from logging import raiseExceptions
from rest_framework.views import APIView
from django.http import FileResponse

from .serializers import materiaSerializer
from .models import Materia
from rest_framework.response import Response
from Pensum.settings import BASE_DIR

import os
# Create your views here.

class materiaView (viewsets.ModelViewSet):
    serializer_class = materiaSerializer
    queryset = Materia.objects.all()

class syllabusFile(APIView):
    def post(self,request,*args,**kwargs):
        carrera = request.data.get("codigo_carrera", "")
        codigo = request.data.get("codigo_materia", "")
        
        ruta = os.path.join(BASE_DIR,"src","syllabus", carrera+codigo+".pdf")

        try:
            return FileResponse(open(ruta,"rb"))
        except:
            return raiseExceptions