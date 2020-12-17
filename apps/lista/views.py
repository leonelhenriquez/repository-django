from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializer import *

# Create your views here.

#API PARA LISTA
    #Obtener todas las listas
class ListaView(APIView):
    serializer_class = ListaSerializer
    def get(self, request):
        lista = Lista.objects.all()
        listaSerializer = ListaSerializer(lista, many=True)
        return Response(listaSerializer.data)

#API PARA TIPO_LISTA
    #Obtener todas las tipo listas
class TipoListaView(APIView):
    serializer_class = Tipo_ListaSerializer
    def get(self, request):
        tipoLista = Tipo_Lista.objects.all()
        tipoListaSerializer = Tipo_ListaSerializer(tipoLista, many=True)
        return Response(tipoListaSerializer.data)