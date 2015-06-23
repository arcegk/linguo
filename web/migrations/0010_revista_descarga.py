# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0009_revista'),
    ]

    operations = [
        migrations.AddField(
            model_name='revista',
            name='descarga',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]
