from rest_framework import serializers
from .models import Materia


class materiaSerializer (serializers.ModelSerializer):
    
    class Meta:
        model = Materia
        fields = (
            'codigo_materia',
            'nombre_materia',
            'creditos',
            'semestre',
            'horas_cl',
            'horas_au',
            'codigo_carrera'
        )
