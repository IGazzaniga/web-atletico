# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-02-03 05:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0010_auto_20180203_0047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articulo',
            name='foto',
            field=models.ImageField(upload_to=''),
        ),
    ]
