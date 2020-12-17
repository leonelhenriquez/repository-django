from django.urls import path
from django.conf.urls import url, include
from .views import *

app_name='lista'
urlpatterns = [
    #Recurso
    path('recursoview', RecursoView.as_view(), name='listaView'),
    path('tiporecursoview', TipoRecursoView.as_view(), name='tipoListaView'),
    path('categoriaview', CategoriaView.as_view(), name='tipoListaView'),
]

