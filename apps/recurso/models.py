from django.db import models
from django.conf import settings

# Create your models here.

class Tipo_Recurso(models.Model):
    id = models.AutoField(primary_key=True, )
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Categoria(models.Model):
    id = models.AutoField(primary_key=True, )
    nombre = models.CharField(max_length=250)
    def __str__(self):
        return self.nombre

class Recurso(models.Model):
    id = models.AutoField(primary_key=True,)
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,)
    titulo = models.CharField(max_length=250)
    descripcion = models.CharField(max_length=250)
    tipo = models.ForeignKey(Tipo_Recurso, on_delete=models.CASCADE)
    year = models.DateField()
    autor = models.CharField(max_length=250)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    fecha = models.DateField()
    imagen = models.ImageField(upload_to='miniaturas', default=None)
    archivo = models.FileField(blank=True, upload_to='files')
    def __str__(self):
        return self.titulo

    class Meta:
        unique_together = [['usuario', 'id']]