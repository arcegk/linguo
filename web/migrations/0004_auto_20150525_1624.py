# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_auto_20150525_1602'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contenido',
            name='imagen',
            field=models.CharField(max_length=100, blank=True),
        ),
    ]
