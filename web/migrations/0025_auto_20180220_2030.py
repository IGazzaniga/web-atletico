# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-02-20 23:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0024_auto_20180220_2024'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tablas',
            name='equipos',
        ),
        migrations.AddField(
            model_name='tablas',
            name='equipos',
            field=models.ManyToManyField(to='web.Equipos_futbol_primera'),
        ),
    ]
