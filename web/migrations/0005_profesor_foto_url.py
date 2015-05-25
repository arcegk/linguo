# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_auto_20150525_1624'),
    ]

    operations = [
        migrations.AddField(
            model_name='profesor',
            name='foto_url',
            field=models.CharField(max_length=200, verbose_name=b'Enlaza una foto!', blank=True),
        ),
    ]
