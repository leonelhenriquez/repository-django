# Generated by Django 3.1.4 on 2020-12-28 21:14

import apps.recurso.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recurso', '0003_auto_20201228_1431'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recurso',
            name='archivo',
            field=models.FileField(blank=True, default=None, upload_to=apps.recurso.models.get_file_name_archivo),
        ),
        migrations.AlterField(
            model_name='recurso',
            name='imagen',
            field=models.ImageField(blank=True, default=None, upload_to=apps.recurso.models.get_file_name_miniatura),
        ),
        migrations.AlterField(
            model_name='recursoarchivo',
            name='filename',
            field=models.TextField(max_length=255),
        ),
        migrations.AlterField(
            model_name='recursoimagen',
            name='filename',
            field=models.TextField(max_length=255),
        ),
    ]