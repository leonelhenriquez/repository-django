# Generated by Django 3.1.4 on 2020-12-28 23:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recurso', '0006_auto_20201228_1517'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recurso',
            name='descripcion',
            field=models.CharField(max_length=500),
        ),
    ]
