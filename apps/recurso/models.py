from datetime import datetime

from db_file_storage.model_utils import delete_file, delete_file_if_needed
from db_file_storage.compat import  reverse
from django.core.validators import MaxValueValidator
from django.db import models
from django.conf import settings
import random
import string
from .util import get_file_name


# Create your models here.

class Tipo_Recurso(models.Model):
    id = models.AutoField(primary_key=True, )
    nombre = models.CharField(max_length=100)
    def __str__(self):
        return self.nombre
    class Meta:
        ordering = ['nombre']

class Categoria(models.Model):
    id = models.AutoField(primary_key=True, )
    nombre = models.CharField(max_length=250)
    def __str__(self):
        return self.nombre
    class Meta:
        ordering = ['nombre']


class RecursoImagen(models.Model):
    id_recurso_imagen = models.AutoField(primary_key=True)
    bytes = models.BinaryField()
    filename = models.CharField(max_length=500)
    mimetype = models.CharField(max_length=50)
    def __str__(self):
        return self.filename

class RecursoArchivo(models.Model):
    id_recurso_archivo = models.AutoField(primary_key=True)
    bytes = models.BinaryField()
    filename = models.CharField(max_length=500)
    mimetype = models.CharField(max_length=50)
    def __str__(self):
        return self.filename

def get_file_name_miniatura(instance, filename):
  return get_file_name(
    base='recurso.RecursoImagen/bytes/filename/mimetype',
    instance=instance, filename=filename
  )

def get_file_name_archivo(instance, filename):
  return get_file_name(
    base='recurso.RecursoArchivo/bytes/filename/mimetype',
    instance=instance, filename=filename
  )

class Recurso(models.Model):
    id = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=250)
    descripcion = models.CharField(max_length=500)
    tipo = models.ForeignKey(Tipo_Recurso, on_delete=models.CASCADE)
    anyo_publicacion = models.IntegerField(validators=[MaxValueValidator(datetime.now().year)])
    autor = models.CharField(max_length=250)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    fecha = models.DateField(auto_now_add=True)
    imagen = models.ImageField(
        upload_to=get_file_name_miniatura,
        blank=True, null=False, default=None, max_length=500
    )
    archivo = models.FileField(
        upload_to=get_file_name_archivo,
        blank=True, null=False, default=None, max_length=500
    )

    def __str__(self):
        return self.titulo

    def save(self, *args, **kwargs):
        delete_file_if_needed(self, 'imagen')
        delete_file_if_needed(self, 'archivo')
        super(Recurso, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        super(Recurso, self).delete(*args, **kwargs)
        delete_file(self, 'imagen')
        delete_file(self, 'archivo')

    class Meta:
        unique_together = [['usuario', 'id']]
        
