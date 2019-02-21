# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-09-20 12:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0002_auto_20180920_1515'),
        ('client', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='home_county',
            field=models.CharField(blank=True, choices=[(b'NAI', b'Nairobi'), (b'KIS', b'Kisumu')], max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='myuser',
            name='school',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='school.School'),
        ),
    ]
