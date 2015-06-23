# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0008_profesor_modalidad'),
    ]

    operations = [
        migrations.CreateModel(
            name='Revista',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('edicion', models.CharField(max_length=25)),
                ('descripcion', models.TextField()),
                ('imagen', models.CharField(max_length=200)),
            ],
        ),
    ]
