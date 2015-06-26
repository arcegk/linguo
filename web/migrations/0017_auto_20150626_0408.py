# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0016_auto_20150626_0402'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='nivel',
            name='modulo',
        ),
        migrations.AddField(
            model_name='modulo',
            name='levels',
            field=models.ManyToManyField(to='web.Nivel'),
        ),
    ]
