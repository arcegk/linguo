# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import aloha.fields


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0011_auto_20150622_1958'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contenido',
            name='texto',
            field=aloha.fields.HTMLField(),
        ),
    ]
