from rest_framework import generics

from apps import recurso
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializer import *
from apps.recurso import serializer

# Create your views here.

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List' : '/recurso-list/',
        'Detail View': '/recurso-detail/<str:pk>/',
        'Create' : '/recurso-create/',
        'Update' : '/recurso-update/<str:pk>/',
        'Delete' : '/recurso-delete/<str:pk>/'
    }
    return Response(api_urls)


#API CRUD Recurso
'''
@api_view(['GET'])
def recursoList(request):
        recursos = Recurso.objects.all();
        serializer = RecursoSerializer(recursos, many=True)
        return Response(serializer.data)
'''

class recursoList(generics.ListAPIView):
    queryset = Recurso.objects.all()
    serializer_class = RecursoDetailSerializer


@api_view(['GET'])
def recursoDetail(request, pk):
    try:
        recursos = Recurso.objects.get(id=pk);
        serializer = RecursoDetailSerializer(recursos)
        return Response(serializer.data)
    except Recurso.DoesNotExist:
        return Response({})

'''
@api_view(['POST'])
def recursoCreate(request):
    serializer = RecursoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
'''
class recursoCreate(generics.CreateAPIView):
    queryset = Recurso.objects.all()
    serializer_class = RecursoSerializer

'''
@api_view(['POST'])
def recursoUpdate(request, pk):
    recurso = Recurso.objects.get(id=pk)
    serializer = RecursoSerializer(instance=recurso, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
'''
class recursoUpdate(generics.RetrieveUpdateAPIView):
    queryset = Recurso.objects.all()
    serializer_class = RecursoSerializer

'''
@api_view(['DELETE'])
def recursoDelete(request, pk):
    try:
        recurso = Recurso.objects.get(id=pk)
        recurso.removed = True
        recurso.save(update_fields=['removed'])
        return Response({
            'removed': True,
        })
    except Recurso.DoesNotExist:
        return Response({
            'removed': False,
        })
'''

class recursoDelete(generics.DestroyAPIView):
    queryset = Recurso.objects.all()
    serializer_class = RecursoSerializer

#API PARA TIPO_Recurso
    #Obtener todas los tipos de recurso
'''
class TipoRecursoView(APIView):
    serializer_class = Tipo_RecursoSerializer
    def get(self, request):
        tipoRecurso = Tipo_Recurso.objects.all()
        tipoRecursoSerializer = Tipo_RecursoSerializer(tipoRecurso, many=True)
        return Response(tipoRecursoSerializer.data)
'''
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

'''
@api_view(['GET'])
def tipoRecursoList(request):
        tipo_recursos = Tipo_Recurso.objects.all();
        serializer = Tipo_RecursoSerializer(tipo_recursos, many=True)
        return Response(serializer.data)
'''

class tipoRecursoList(generics.ListAPIView):
    queryset = Tipo_Recurso.objects.all().order_by('nombre')
    serializer_class = Tipo_RecursoSerializer

@api_view(['GET'])
def tipoRecursoDetail(request, pk):
        tipo_recursos = Tipo_Recurso.objects.all(id=pk);
        serializer = Tipo_RecursoSerializer(tipo_recursos, many=False)
        return Response(serializer.data)

'''
@api_view(['POST'])
def tipoRecursoCreate(request):
    serializer = Tipo_RecursoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
'''

class tipoRecursoCreate(generics.CreateAPIView):
    queryset = Tipo_Recurso.objects.all().order_by('nombre')
    serializer_class = Tipo_RecursoSerializer

'''
@api_view(['POST'])
def tipoRecursoUpdate(request, pk):
    tipo_recurso = Tipo_Recurso.objects.get(id=pk)
    serializer = Tipo_RecursoSerializer(instance=tipo_recurso, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
'''

class tipoRecursoUpdate(generics.RetrieveUpdateAPIView):
    queryset = Tipo_Recurso.objects.all().order_by('nombre')
    serializer_class = Tipo_RecursoSerializer

'''
@api_view(['DELETE'])
def tipoRecursoDelete(request, pk):
    tipo_recurso = Tipo_RecursoSerializer.objects.get(id=pk)
    tipo_recurso.delete()
    return Response('Tipo Recurso Eliminado!')
'''

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
'''
@api_view(['GET'])
def categoriaList(request):
        categorias  = Categoria.objects.all();
        serializer = CategoriaSerializer(categorias, many=True)
        return Response(serializer.data)
'''
class categoriaList(generics.ListAPIView):
    queryset = Categoria.objects.all().order_by('nombre')
    serializer_class = CategoriaSerializer

@api_view(['GET'])
def categoriaDetail(request, pk):
        categorias = Categoria.objects.all(id=pk);
        serializer = CategoriaSerializer(categorias, many=False)
        return Response(serializer.data)
'''
@api_view(['POST'])
def categoriaCreate(request):
    serializer = CategoriaSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
'''
class categoriaCreate(generics.CreateAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

'''
@api_view(['POST'])
def categoriaUpdate(request, pk):
    categoria = Categoria.objects.get(id=pk)
    serializer = CategoriaSerializer(instance=categoria, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
'''

class categoriaUpdate(generics.RetrieveUpdateAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

'''
@api_view(['DELETE'])
def categoriaDelete(request, pk):
    categoria = Categoria.objects.get(id=pk)
    categoria.delete()
    return Response('Categoria Eliminada!')
'''

class categoriaDelete(generics.DestroyAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer