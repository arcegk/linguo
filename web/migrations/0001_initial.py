# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Idioma',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=25)),
                ('nivel', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Profesor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=25)),
                ('direccion', models.CharField(max_length=25)),
                ('telefono', models.CharField(max_length=15)),
                ('lugar_apredizaje', models.CharField(max_length=50)),
                ('estudios', models.TextField(max_length=50)),
                ('referencia_personal_1', models.CharField(max_length=100, verbose_name=b'Referencia personal 1')),
                ('referencia_personal_2', models.CharField(max_length=100, verbose_name=b'Referencia personal 2')),
                ('referencia_come_1', models.CharField(max_length=100, verbose_name=b'Referencia personal 1')),
                ('referencia_come_2', models.CharField(max_length=100, verbose_name=b'Referencia personal 1')),
                ('idioma', models.ManyToManyField(to='web.Idioma')),
            ],
        ),
    ]
