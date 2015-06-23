# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0005_profesor_foto_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='Modalidad',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('modalidad', models.CharField(max_length=25)),
            ],
        ),
        migrations.AddField(
            model_name='profesor',
            name='experiencia',
            field=models.CharField(default='', max_length=70),
            preserve_default=False,
        ),
    ]
