# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0007_profesor_sector'),
    ]

    operations = [
        migrations.AddField(
            model_name='profesor',
            name='modalidad',
            field=models.ManyToManyField(to='web.Modalidad'),
        ),
    ]
