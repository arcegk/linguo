# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0012_auto_20150622_2108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contenido',
            name='texto',
            field=models.TextField(),
        ),
    ]
