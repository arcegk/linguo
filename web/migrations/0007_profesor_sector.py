# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0006_auto_20150622_1628'),
    ]

    operations = [
        migrations.AddField(
            model_name='profesor',
            name='sector',
            field=models.CharField(default='', max_length=25, choices=[(b'SUR', b'SUR'), (b'NORTE', b'NORTE'), (b'ORIENTE', b'ORIENTE'), (b'OCCIDENTE', b'OCCIDENTE')]),
            preserve_default=False,
        ),
    ]
