# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0015_auto_20150622_2150'),
    ]

    operations = [
        migrations.CreateModel(
            name='Modulo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('modulo', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Nivel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nivel', models.CharField(max_length=25)),
                ('texto', ckeditor.fields.RichTextField()),
                ('modulo', models.ForeignKey(to='web.Modulo')),
            ],
        ),
        migrations.AlterField(
            model_name='contenido',
            name='seccion',
            field=models.CharField(max_length=25, choices=[(b'INICIO', b'INICIO'), (b'REVISTA', b'REVISTA'), (b'RECURSOS', b'RECURSOS'), (b'SERVICIOS', b'SERVICIOS'), (b'PROFESORES', b'PROFESORES'), (b'RECURSOS-NOTICIAS', b'RECURSOS-NOTICIAS')]),
        ),
    ]
