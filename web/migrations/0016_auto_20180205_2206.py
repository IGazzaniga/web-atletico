# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-02-06 01:06
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0015_auto_20180205_2201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articulo',
            name='cuerpo',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
