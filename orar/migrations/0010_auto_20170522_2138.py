# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-22 21:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orar', '0009_event_serie'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='end_hour',
            field=models.CharField(default='10:00', max_length=5),
        ),
        migrations.AlterField(
            model_name='event',
            name='start_hour',
            field=models.CharField(default='8:00', max_length=5),
        ),
    ]