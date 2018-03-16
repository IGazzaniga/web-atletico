# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-02-03 03:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0009_auto_20180115_0104'),
    ]

    operations = [
        migrations.CreateModel(
            name='Equipos_futbol_senior',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('puntos_torneo', models.IntegerField(default=0)),
                ('puntos_general', models.IntegerField(default=0)),
                ('p_jugados_torneo', models.IntegerField(default=0)),
                ('p_jugados_general', models.IntegerField(default=0)),
                ('p_ganados_torneo', models.IntegerField(default=0)),
                ('p_ganados_general', models.IntegerField(default=0)),
                ('p_empatados_torneo', models.IntegerField(default=0)),
                ('p_empatados_general', models.IntegerField(default=0)),
                ('p_perdidos_torneo', models.IntegerField(default=0)),
                ('p_perdidos_general', models.IntegerField(default=0)),
                ('goles_favor_torneo', models.IntegerField(default=0)),
                ('goles_favor_general', models.IntegerField(default=0)),
                ('goles_contra_torneo', models.IntegerField(default=0)),
                ('goles_contra_general', models.IntegerField(default=0)),
                ('dif_gol_torneo', models.IntegerField(default=0)),
                ('dif_gol_general', models.IntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='articulo',
            name='slug',
            field=models.SlugField(default='', unique=True),
        ),
        migrations.AlterField(
            model_name='articulo',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]