# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-22 20:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orar', '0005_auto_20170522_2041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='day',
            field=models.IntegerField(choices=[(1, 'Luni'), (2, 'Marti'), (3, 'Miercuri'), (4, 'Joi'), (5, 'Vineri')], default=1),
        ),
    ]
