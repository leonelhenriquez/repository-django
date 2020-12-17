from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.
class Tipo_Lista(models.Model):
    id = models.AutoField(primary_key=True,)
    nombre = models.CharField(max_length=100)
    def __str__(self):
        return self.nombre

class Lista(models.Model):
    id = models.AutoField(primary_key=True,)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE,)
    tipo = models.ForeignKey(Tipo_Lista, on_delete=models.CASCADE)
    fecha = models.DateField()
    def __str__(self):
        return self.tipo
    class Meta:
        unique_together = [['usuario', 'id']]
