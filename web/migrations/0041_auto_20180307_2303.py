# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-03-08 02:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0040_auto_20180223_2133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='torneo',
            name='nombre',
            field=models.CharField(choices=[('Primera', 'Primera'), ('Sub-21', 'Sub-21'), ('General Primera', 'General Primera'), ('General Sub-21', 'General Sub-21'), ('Novena', 'Novena'), ('Octava', 'Octava'), ('Septima', 'Septima'), ('Sexta', 'Sexta'), ('General Inferiores', 'General Inferiores'), ('Senior', 'Senior'), ('General Senior', 'General Senior'), ('Hockey Primera', 'Hockey Primera'), ('Hockey Sexta', 'Hockey Sexta'), ('Hockey Septima', 'Hockey Septima')], max_length=200),
        ),
    ]