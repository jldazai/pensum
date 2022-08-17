from tkinter import CASCADE
from django.db import models

from carreras.models import Carrera
# Create your models here.
class Materia (models.Model):
    codigo_materia = models.CharField(primary_key=True, max_length=6)
    nombre_materia = models.CharField(max_length=30)
    creditos = models.IntegerField()
    semestre = models.IntegerField()
    horas_cl = models.IntegerField()
    horas_au = models.IntegerField()
    
    codigo_carrera = models.ForeignKey(Carrera, on_delete=models.CASCADE)