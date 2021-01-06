from django.urls import path
from django.conf.urls import url, include
from .views import *
from apps.recurso import views

app_name='lista'
urlpatterns = [
    #CRUD Recurso
    path('recurso-list/', views.recursoList.as_view(), name="recurso-list"),
    path('recurso-userlist/<int:user>/', views.recursoUserList, name="recurso-userlist"),
    path('recurso-detail/<str:pk>/', views.recursoDetail, name="recurso-detail"),
    path('recurso-create/', views.recursoCreate.as_view(), name='recurso-create'),
    path('recurso-update/<str:pk>/', views.recursoUpdate.as_view(), name='recurso-update'),
    path('recurso-delete/<str:pk>/', views.recursoDelete.as_view(), name='recurso-delete'),
    #CRUD Tipo Recurso
    path('tipoRecurso-list/', views.tipoRecursoList.as_view(), name="tipoRecurso-list"),
    path('tipoRecurso-detail/<str:pk>/', views.tipoRecursoDetail, name="tipoRecurso-detail"),
    path('tipoRecurso-create/', views.tipoRecursoCreate.as_view(), name='tipoRecurso-create'),
    path('tipoRecurso-update/<str:pk>/', views.tipoRecursoUpdate.as_view(), name='tipoRecurso-update'),
    path('tipoRecurso-delete/<str:pk>/', views.tipoRecursoDelete.as_view(), name='tipoRecurso-delete'),
    #CRUD Categoria
    path('categoria-list/', views.categoriaList.as_view(), name="categoria-list"),
    path('categoria-detail/<str:pk>/', views.categoriaDetail, name="categoria-detail"),
    path('categoria-create/', views.categoriaCreate.as_view(), name='categoria-create'),
    path('categoria-update/<str:pk>/', views.categoriaUpdate.as_view(), name='categoria-update'),
    path('categoria-delete/<str:pk>/', views.categoriaDelete.as_view(), name='categoria-delete')
]

