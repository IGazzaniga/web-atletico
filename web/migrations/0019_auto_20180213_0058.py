# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-02-13 03:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0018_auto_20180213_0046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articulo',
            name='url_video',
            field=models.CharField(blank=True, max_length=300, verbose_name='Url del video de youtube (opcional)'),
        ),
    ]
