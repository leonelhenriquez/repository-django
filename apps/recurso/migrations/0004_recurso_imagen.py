# Generated by Django 3.1.4 on 2020-12-23 03:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recurso', '0003_auto_20201216_0006'),
    ]

    operations = [
        migrations.AddField(
            model_name='recurso',
            name='imagen',
            field=models.ImageField(default=None, upload_to='miniaturas'),
        ),
    ]
