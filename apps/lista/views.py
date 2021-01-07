from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializer import *
from rest_framework import generics

# Create your views here.

'''
@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List':'/task-detail/<str:pk>/',
        'Detail view':'/task-detail/<str:pk>/',
        'Create':'/task-create/',
        'Update':'/task-update/<str:pk>/',
        'Delete':'/task-delete/<str:pk>/',

    }
    return Response(api_urls)

'''
########################## API's FOR LISTA ###############################

'''
@api_view(['GET'])
def listaListas(APIView):
    listas = Lista.objects.all()
    serializer = ListaSerializer(listas, many=True)
    return Response(serializer.data)
'''
'''
class listaListas(generics.ListAPIView):
    queryset = Lista.objects.all()
    serializer_class = ListaSerializer
'''
@api_view(['GET'])
def listaListas(request, idUsuario, tipo):
    listas = Lista.objects.filter(usuario=idUsuario, tipo=tipo).order_by('-fecha','-id')
    serializer = ListaDetailSerializer(listas, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def listaListasNoDetail(request, idUsuario, tipo):
    listas = Lista.objects.filter(usuario=idUsuario, tipo=tipo).order_by('-fecha','-id')
    serializer = ListaDetailSerializer__Tipo(listas, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def listaDetail(request, idUsuario, tipo, recurso):
    try:
        tasks = Lista.objects.get(usuario=idUsuario, tipo=tipo, recurso=recurso)
        serializer = ListaDetailSerializer__Tipo(tasks, many=False)
        return Response(serializer.data)
    except Lista.DoesNotExist:
        return Response({})

'''
@api_view(['POST'])
def listaCreate(request):
	serializer = ListaSerializer(data=request.data)
	if serializer.is_valid():
		serializer.save()
	return Response(serializer.data)
'''
class listaCreate(generics.CreateAPIView):
    queryset = Lista.objects.all()
    serializer_class = ListaSerializer

'''
@api_view(['POST'])
def listaUpdate(request, pk):
	task = Lista.objects.get(id=pk)
	serializer = ListaSerializer(instance=task, data=request.data)
	if serializer.is_valid():
		serializer.save()
	return Response(serializer.data)
'''

class listaUpdate(generics.RetrieveUpdateAPIView):
    queryset = Lista.objects.all()
    serializer_class = ListaSerializer

'''
@api_view(['DELETE'])
def listaDelete(request, pk):
	task = Lista.objects.get(id=pk)
	task.delete()
	return Response('succsesfully deleted')
'''

class listaDelete(generics.DestroyAPIView):
    queryset = Lista.objects.all()
    serializer_class = ListaSerializer

########################## API's FOR LISTA ###############################


########################## API's FOR TIPO_LISTA ###############################
'''
@api_view(['GET'])
def tipolistaListas(request):
    listas = Tipo_Lista.objects.all()
    serializer = Tipo_ListaSerializer(listas, many=True)
    return Response(serializer.data)
'''
class tipolistaListas(generics.ListAPIView):
    queryset = Tipo_Lista.objects.all()
    serializer_class = Tipo_ListaSerializer

@api_view(['GET'])
def tipolistaDetail(request, pk):
	tasks = Tipo_Lista.objects.get(id=pk)
	serializer = Tipo_ListaSerializer(tasks, many=False)
	return Response(serializer.data)

'''
@api_view(['POST'])
def tipolistaCreate(request):
	serializer = Tipo_ListaSerializer(data=request.data)
	if serializer.is_valid():
		serializer.save()
	return Response(serializer.data)
'''
class tipolistaCreate(generics.CreateAPIView):
    queryset = Tipo_Lista.objects.all()
    serializer_class = Tipo_ListaSerializer
'''
@api_view(['POST'])
def tipolistaUpdate(request, pk):
	task = Tipo_Lista.objects.get(id=pk)
	serializer = Tipo_ListaSerializer(instance=task, data=request.data)
	if serializer.is_valid():
		serializer.save()
	return Response(serializer.data)
'''

class tipolistaUpdate(generics.RetrieveUpdateAPIView):
    queryset = Tipo_Lista.objects.all()
    serializer_class = Tipo_ListaSerializer

'''
@api_view(['DELETE'])
def tipolistaDelete(request, pk):
	task = Tipo_Lista.objects.get(id=pk)
	task.delete()
	return Response('succsesfully deleted')
'''

class tipolistaDelete(generics.DestroyAPIView):
    queryset = Tipo_Lista.objects.all()
    serializer_class = Tipo_ListaSerializer

########################## API's FOR TIPO_LISTA ###############################

########################## API's FOR LISTA_LIBRO ###############################

class lista_LibroListas(generics.ListAPIView):
    queryset = Lista_Libro.objects.all()
    serializer_class = Lista_LibroSerializer

@api_view(['GET'])
def lista_LibroDetail(request, pk):
	tasks = Lista_Libro.objects.get(id=pk)
	serializer = Lista_LibroSerializer(tasks, many=False)
	return Response(serializer.data)

class lista_LibroCreate(generics.CreateAPIView):
    queryset = Lista_Libro.objects.all()
    serializer_class = Lista_LibroSerializer

class lista_LibroUpdate(generics.RetrieveUpdateAPIView):
    queryset = Lista_Libro.objects.all()
    serializer_class = Lista_LibroSerializer

class lista_LibroDelete(generics.DestroyAPIView):
    queryset = Lista_Libro.objects.all()
    serializer_class = Lista_LibroSerializer