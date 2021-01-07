from django.urls import path
from django.conf.urls import url, include
from .views import *
from . import views


urlpatterns = [
  #listas
	path('lista-listas/<int:idUsuario>/<int:tipo>/', views.listaListas, name='api-overview-lista'),
	path('lista-listas_nodetail/<int:idUsuario>/<int:tipo>/', views.listaListasNoDetail, name='api-overview-lista'),
	path('lista-detail/<int:idUsuario>/<int:tipo>/<int:recurso>/', views.listaDetail, name="lista-detail"),
	path('lista-add/', views.listaCreate.as_view(), name="lista-create"),
	#path('lista-update/<str:pk>/', views.listaUpdate.as_view(), name="lista-update"),
	path('lista-delete/<str:pk>/', views.listaDelete.as_view(), name="lista-delete"),
    #tipo listas
	path('tipo-lista-listas/', views.tipolistaListas.as_view(), name='api-overview-tipo-lista'),
	path('tipo-lista-detail/<str:pk>/', views.tipolistaDetail, name="tipo-lista-detail"),
	path('tipo-lista-create/', views.tipolistaCreate.as_view(), name="tipo-lista-create"),
	path('tipo-lista-update/<str:pk>/', views.tipolistaUpdate.as_view(), name="tipo-lista-update"),
	path('tipo-lista-delete/<str:pk>/', views.tipolistaDelete.as_view(), name="tipo-lista-delete"),
	#lista-libro
 	path('lista-libro-list/', views.lista_LibroListas.as_view(), name='lista-libro-list'),
  	path('lista-libro-detail/<str:pk>/', views.lista_LibroDetail, name="lista-libro-detail"),
	path('lista-libro-create/', views.lista_LibroCreate.as_view(), name="lista-libro-create"),
	path('lista-libro-update/<str:pk>/', views.lista_LibroUpdate.as_view(), name="lista-libro-update"),
	path('lista-libro-delete/<str:pk>/', views.lista_LibroDelete.as_view(), name="lista-libro-delete"),
]