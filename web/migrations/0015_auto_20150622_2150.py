# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0014_auto_20150622_2133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contenido',
            name='texto',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
