# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-02-21 21:49
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0032_auto_20180221_1636'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Equipos_futbol_primera',
            new_name='Equipos',
        ),
        migrations.DeleteModel(
            name='Equipos_futbol_senior',
        ),
        migrations.DeleteModel(
            name='Equipos_futbol_sub21',
        ),
    ]
