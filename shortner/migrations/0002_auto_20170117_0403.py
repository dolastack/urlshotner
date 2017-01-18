# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-17 04:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortner', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='kirrurl',
            name='actve',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='kirrurl',
            name='shotcode',
            field=models.CharField(blank=True, max_length=15, unique=True),
        ),
    ]