# Generated by Django 3.1.4 on 2020-12-28 02:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recurso', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recursoarchivo',
            old_name='recurso_archivo_pk',
            new_name='id_recurso_archivo',
        ),
        migrations.RenameField(
            model_name='recursoimagen',
            old_name='recurso_imagen_pk',
            new_name='id_recurso_imagen',
        ),
    ]
