from rest_framework import generics

from apps import recurso
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.filters import SearchFilter, OrderingFilter
from .models import *
from .serializer import *
from apps.recurso import serializer



# Create your views here.

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List' : '/recurso-list/',
        'User List' : '/recurso-userlist/<int:user>/',
        'Detail View': '/recurso-detail/<str:pk>/',
        'Create' : '/recurso-create/',
        'Update' : '/recurso-update/<str:pk>/',
        'Delete' : '/recurso-delete/<str:pk>/'
    }
    return Response(api_urls)


#API CRUD Recurso

class recursoList(generics.ListAPIView):
    queryset = Recurso.objects.all().order_by('-fecha','-id')
    serializer_class = RecursoDetailSerializer

    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('titulo','descripcion', 'tipo__nombre', 'autor', 'categoria__nombre')
    
@api_view(['GET'])
def recursoUserList(request, user):
    recursos = Recurso.objects.filter(usuario=user).order_by('-fecha','-id')
    serializer = RecursoDetailSerializer(recursos, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def recursoDetail(request, pk):
    try:
        recursos = Recurso.objects.get(id=pk);
        serializer = RecursoDetailSerializer(recursos)
        return Response(serializer.data)
    except Recurso.DoesNotExist:
        return Response({})

class recursoCreate(generics.CreateAPIView):
    queryset = Recurso.objects.all()
    serializer_class = RecursoSerializer

class recursoUpdate(generics.RetrieveUpdateAPIView):
    queryset = Recurso.objects.all()
    serializer_class = RecursoSerializer


class recursoDelete(generics.DestroyAPIView):
    queryset = Recurso.objects.all()
    serializer_class = RecursoSerializer

#API PARA TIPO_Recurso
    #Obtener todas los tipos de recurso

class TipoRecursoView(generics.ListAPIView):
    queryset = Tipo_Recurso.objects.all()
    serializer_class = Tipo_RecursoSerializer

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List' : '/tipoRecurso-list/',
        'Detail View': '/tipoRecurso-detail/<str:pk>/',
        'Create' : '/tipoRecurso-create/',
        'Update' : '/tipoRecurso-update/<str:pk>/',
        'Delete' : '/tipoRecurso-delete/<str:pk>/'
    }
    return Response(api_urls)

#API CRUD Tipo Recurso

class tipoRecursoList(generics.ListAPIView):
    queryset = Tipo_Recurso.objects.all().order_by('nombre')
    serializer_class = Tipo_RecursoSerializer

@api_view(['GET'])
def tipoRecursoDetail(request, pk):
    tipo_recursos = Tipo_Recurso.objects.all(id=pk);
    serializer = Tipo_RecursoSerializer(tipo_recursos, many=False)
    return Response(serializer.data)

class tipoRecursoCreate(generics.CreateAPIView):
    queryset = Tipo_Recurso.objects.all().order_by('nombre')
    serializer_class = Tipo_RecursoSerializer

class tipoRecursoUpdate(generics.RetrieveUpdateAPIView):
    queryset = Tipo_Recurso.objects.all().order_by('nombre')
    serializer_class = Tipo_RecursoSerializer

class tipoRecursoDelete(generics.DestroyAPIView):
    queryset = Tipo_Recurso.objects.all()
    serializer_class = Tipo_RecursoSerializer

#API PARA Categoria
    #Obtener todas las categorias
class CategoriaView(APIView):
    serializer_class = CategoriaSerializer
    def get(self, request):
        categoria = Categoria.objects.all()
        categoriaSerializer = Tipo_RecursoSerializer(categoria, many=True)
        return Response(categoriaSerializer.data)

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List' : '/categoria-list/',
        'Detail View': '/categoria-detail/<str:pk>/',
        'Create' : '/categoria-create/',
        'Update' : '/categoria-update/<str:pk>/',
        'Delete' : '/categoria-delete/<str:pk>/'
    }
    return Response(api_urls)

#API CRUD Categoria

class categoriaList(generics.ListAPIView):
    queryset = Categoria.objects.all().order_by('nombre')
    serializer_class = CategoriaSerializer

@api_view(['GET'])
def categoriaDetail(request, pk):
    categorias = Categoria.objects.all(id=pk);
    serializer = CategoriaSerializer(categorias, many=False)
    return Response(serializer.data)

class categoriaCreate(generics.CreateAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class categoriaUpdate(generics.RetrieveUpdateAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class categoriaDelete(generics.DestroyAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer