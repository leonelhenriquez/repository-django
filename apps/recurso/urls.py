from django.urls import path
from django.conf.urls import url, include
from .views import *
from apps.recurso import views

app_name='lista'
urlpatterns = [
    #Recurso
    path('recursoview', RecursoView.as_view(), name='recursoView'),
    path('tiporecursoview', TipoRecursoView.as_view(), name='tipoRecursoView'),
    path('categoriaview', CategoriaView.as_view(), name='categoriaView'),
    #CRUD Recurso
    path('recurso-list/', views.recursoList, name="recurso-list"),
    path('recurso-detail/<str:pk>/', views.recursoDetail, name="recurso-detail"),
    path('recurso-create/', views.recursoCreate, name='recurso-create'),
    path('recurso-update/<str:pk>/', views.recursoUpdate, name='recurso-update'),
    path('recurso-delete/<str:pk>/', views.recursoDelete, name='recurso-delete'),
    #CRUD Tipo Recurso
    path('tipoRecurso-list/', views.tipoRecursoList, name="tipoRecurso-list"),
    path('tipoRecurso-detail/<str:pk>/', views.tipoRecursoDetail, name="tipoRecurso-detail"),
    path('tipoRecurso-create/', views.tipoRecursoCreate, name='tipoRecurso-create'),
    path('tipoRecurso-update/<str:pk>/', views.tipoRecursoUpdate, name='tipoRecurso-update'),
    path('tipoRecurso-delete/<str:pk>/', views.tipoRecursoDelete, name='tipoRecurso-delete'),
    #CRUD Categoria
    path('categoria-list/', views.categoriaList, name="categoria-list"),
    path('categoria-detail/<str:pk>/', views.categoriaDetail, name="categoria-detail"),
    path('categoria-create/', views.categoriaCreate, name='categoria-create'),
    path('categoria-update/<str:pk>/', views.categoriaUpdate, name='categoria-update'),
    path('categoria-delete/<str:pk>/', views.categoriaDelete, name='categoria-delete')
]

