# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-29 21:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orar', '0010_auto_20170522_2138'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='weekly',
            field=models.BooleanField(default=True),
        ),
    ]
