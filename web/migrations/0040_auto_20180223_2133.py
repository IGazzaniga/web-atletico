# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-02-24 00:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0039_auto_20180223_0123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articulo',
            name='album_flickr',
            field=models.CharField(blank=True, help_text="Subir fotos a Flickr, crear un álbum, compartirlo eligiendo la opción 'Insertar', elegir el tamaño más grande, y pegar el link aquí", max_length=700),
        ),
    ]
