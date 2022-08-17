from django.db import models

# Create your models here.
class Carrera (models.Model):
    codigo_carrera = models.CharField(primary_key=True, max_length=6)
    nombre_carrera = models.CharField(max_length=30)
    total_creditos = models.IntegerField()
