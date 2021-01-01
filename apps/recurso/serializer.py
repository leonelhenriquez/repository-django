from rest_framework import serializers
from .models import *
from apps.usuario.serializer import UserSerializer


class RecursoSerializer(serializers.ModelSerializer):
    class Meta:
        many = False
        model = Recurso
        fields = '__all__'

class Tipo_RecursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tipo_Recurso
        fields = '__all__'

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'

class RecursoDetailSerializer(serializers.ModelSerializer):
    tipo = Tipo_RecursoSerializer(read_only=True)
    categoria = CategoriaSerializer(read_only=True)
    usuario = UserSerializer(read_only=True)
    class Meta:
        many = True
        model = Recurso
        fields = '__all__'