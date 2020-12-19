from django.urls import path
from django.conf.urls import url, include
from .views import *
from . import views

app_name='lista'

urlpatterns = [
    #CRUD EMPRESA
    path('listaview', ListaView.as_view(), name='listaView'),
    path('tipolistaview', TipoListaView.as_view(), name='tipoListaView'),
    path('', views.apiOverview, name='api-overview'),
    #listas
    path('lista-listas/', views.listaListas, name='api-overview'),
    path('lista-detail/<str:pk>/', views.listaDetail, name="lista-detail"),
	path('lista-create/', views.listaCreate, name="lista-create"),
	path('lista-update/<str:pk>/', views.listaUpdate, name="lista-update"),
	path('lista-delete/<str:pk>/', views.listaDelete, name="lista-delete"),
    #tipo listas
    path('tipo-lista-listas/', views.tipolistaListas, name='api-overview'),
    path('tipo-lista-detail/<str:pk>/', views.tipolistaDetail, name="tipo-lista-detail"),
	path('tipo-lista-create/', views.tipolistaCreate, name="tipo-lista-create"),
	path('tipo-lista-update/<str:pk>/', views.tipolistaUpdate, name="tipo-lista-update"),
	path('tipo-lista-delete/<str:pk>/', views.tipolistaDelete, name="tipo-lista-delete"),
]