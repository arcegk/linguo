# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contenido',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=50)),
                ('texto', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='profesor',
            name='estudios',
            field=models.TextField(max_length=350),
        ),
    ]
