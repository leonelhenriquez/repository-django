# Generated by Django 3.1.4 on 2021-01-01 00:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recurso', '0009_recurso_removed'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recurso',
            name='removed',
        ),
    ]
