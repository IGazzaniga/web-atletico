# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-02-13 03:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0016_auto_20180205_2206'),
    ]

    operations = [
        migrations.AddField(
            model_name='articulo',
            name='url_video',
            field=models.URLField(blank=True),
        ),
    ]
