# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-09-20 12:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='school',
            name='county',
            field=models.CharField(choices=[(b'NAI', b'Nairobi'), (b'KIS', b'Kisumu')], max_length=30),
        ),
    ]
