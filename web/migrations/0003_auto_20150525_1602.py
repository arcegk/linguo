# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_auto_20150525_1550'),
    ]

    operations = [
        migrations.AddField(
            model_name='contenido',
            name='imagen',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contenido',
            name='seccion',
            field=models.CharField(default='', max_length=25, choices=[(b'INICIO', b'INICIO'), (b'REVISTA', b'REVISTA'), (b'RECURSOS', b'RECURSOS'), (b'SERVICIOS', b'SERVICIOS'), (b'PROFESORES', b'PROFESORES')]),
            preserve_default=False,
        ),
    ]
