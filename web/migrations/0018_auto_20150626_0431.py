# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0017_auto_20150626_0408'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modulo',
            name='levels',
            field=models.ManyToManyField(to='web.Nivel', blank=True),
        ),
        migrations.AlterField(
            model_name='profesor',
            name='referencia_come_1',
            field=models.CharField(max_length=100, verbose_name=b'Referencia personal 1', blank=True),
        ),
        migrations.AlterField(
            model_name='profesor',
            name='referencia_come_2',
            field=models.CharField(max_length=100, verbose_name=b'Referencia personal 1', blank=True),
        ),
        migrations.AlterField(
            model_name='profesor',
            name='referencia_personal_1',
            field=models.CharField(max_length=100, verbose_name=b'Referencia personal 1', blank=True),
        ),
        migrations.AlterField(
            model_name='profesor',
            name='referencia_personal_2',
            field=models.CharField(max_length=100, verbose_name=b'Referencia personal 2', blank=True),
        ),
    ]
