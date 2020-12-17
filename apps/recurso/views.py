from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializer import *

# Create your views here.

#API PARA Recurso
    #Obtener todas los recursos
class RecursoView(APIView):
    serializer_class = RecursoSerializer
    def get(self, request):
        recurso = Recurso.objects.all()
        recursoSerializer = RecursoSerializer(recurso, many=True)
        return Response(recursoSerializer.data)

#API PARA TIPO_Recurso
    #Obtener todas los tipos de recurso
class TipoRecursoView(APIView):
    serializer_class = Tipo_RecursoSerializer
    def get(self, request):
        tipoRecurso = Tipo_Recurso.objects.all()
        tipoRecursoSerializer = Tipo_RecursoSerializer(tipoRecurso, many=True)
        return Response(tipoRecursoSerializer.data)

#API PARA Categoria
    #Obtener todas las categorias
class CategoriaView(APIView):
    serializer_class = CategoriaSerializer
    def get(self, request):
        categoria = Categoria.objects.all()
        categoriaSerializer = Tipo_RecursoSerializer(categoria, many=True)
        return Response(categoriaSerializer.data)