# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-29 21:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orar', '0011_event_weekly'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='tip_saptamana',
            field=models.IntegerField(blank=True, choices=[(1, 'Saptamana Para'), (2, 'Saptamana Imapara')], null=True),
        ),
    ]
