# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-17 04:13
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shortner', '0002_auto_20170117_0403'),
    ]

    operations = [
        migrations.RenameField(
            model_name='kirrurl',
            old_name='actve',
            new_name='active',
        ),
    ]
