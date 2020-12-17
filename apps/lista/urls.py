from django.urls import path
from django.conf.urls import url, include
from .views import *

app_name='lista'

urlpatterns = [
    #CRUD EMPRESA
    path('listaview', ListaView.as_view(), name='listaView'),
    path('tipolistaview', TipoListaView.as_view(), name='tipoListaView'),
]