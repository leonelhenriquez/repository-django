from rest_framework import serializers
from .models import *
from apps.recurso.serializer import RecursoDetailSerializer


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

class ListaDetailSerializer(serializers.ModelSerializer):
    recurso = RecursoDetailSerializer(read_only=True)
    tipo = Tipo_ListaSerializer(read_only=True)
    class Meta:
        many=True
        model = Lista
        fields = '__all__'