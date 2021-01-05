from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from apps.recurso.models import *

# Create your models here.
class Tipo_Lista(models.Model):
    id = models.AutoField(primary_key=True,)
    nombre = models.CharField(max_length=100)
    def __str__(self):
        return self.nombre

class Lista(models.Model):
    id = models.AutoField(primary_key=True,)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    recurso = models.ForeignKey(Recurso, on_delete=models.SET_NULL, null=True)
    tipo = models.ForeignKey(Tipo_Lista, on_delete=models.CASCADE)
    fecha = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.tipo
    class Meta:
        unique_together = [['usuario', 'id']]

class Lista_Libro(models.Model):
    id = models.AutoField(primary_key=True,)
    usuario = models.ForeignKey(User,  on_delete=models.SET_NULL, null=True )
    lista = models.ForeignKey(Lista, on_delete=models.SET_NULL, null=True)
    recurso = models.ForeignKey(Recurso, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return (self.lista + " " + self.recurso)
    class Meta:
        unique_together = [['lista', 'recurso']]