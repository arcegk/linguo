# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0010_revista_descarga'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contenido',
            name='texto',
            field=tinymce.models.HTMLField(),
        ),
    ]
