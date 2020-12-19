from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.decorators import api_view
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


########################## API's FOR LISTA ###############################
@api_view(['GET'])
def listaListas(request):
    listas = Lista.objects.all()
    serializer = ListaSerializer(listas, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def listaDetail(request, pk):
	tasks = Lista.objects.get(id=pk)
	serializer = ListaSerializer(tasks, many=False)
	return Response(serializer.data)


@api_view(['POST'])
def listaCreate(request):
	serializer = ListaSerializer(data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)

@api_view(['POST'])
def listaUpdate(request, pk):
	task = Lista.objects.get(id=pk)
	serializer = ListaSerializer(instance=task, data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)


@api_view(['DELETE'])
def listaDelete(request, pk):
	task = Lista.objects.get(id=pk)
	task.delete()

	return Response('succsesfully deleted')
########################## API's FOR LISTA ###############################


########################## API's FOR TIPO_LISTA ###############################
@api_view(['GET'])
def tipolistaListas(request):
    listas = Tipo_Lista.objects.all()
    serializer = Tipo_ListaSerializer(listas, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def tipolistaDetail(request, pk):
	tasks = Tipo_Lista.objects.get(id=pk)
	serializer = Tipo_ListaSerializer(tasks, many=False)
	return Response(serializer.data)


@api_view(['POST'])
def tipolistaCreate(request):
	serializer = Tipo_ListaSerializer(data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)

@api_view(['POST'])
def tipolistaUpdate(request, pk):
	task = Tipo_Lista.objects.get(id=pk)
	serializer = Tipo_ListaSerializer(instance=task, data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)


@api_view(['DELETE'])
def tipolistaDelete(request, pk):
	task = Tipo_Lista.objects.get(id=pk)
	task.delete()

	return Response('succsesfully deleted')
########################## API's FOR TIPO_LISTA ###############################