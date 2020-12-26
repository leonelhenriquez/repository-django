from rest_framework import serializers
from .models import *


class ListaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lista
        fields = '__all__'

class Tipo_ListaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tipo_Lista
        fields = '__all__'

class Lista_LibroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lista_Libro
        fields = '__all__'