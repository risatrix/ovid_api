# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-04-22 17:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20170422_1725'),
    ]

    operations = [
        migrations.AlterField(
            model_name='line',
            name='text',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
