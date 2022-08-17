from rest_framework import serializers
from .models import Carrera


class carreraSerializer (serializers.ModelSerializer):
    
    class Meta:
        model = Carrera
        fields = (
            'codigo_carrera',
            'nombre_carrera',
            'total_creditos'
        )
