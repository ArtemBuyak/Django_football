# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-22 08:04
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('football', '0002_auto_20170821_1433'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cup',
            old_name='cup',
            new_name='referee',
        ),
        migrations.AlterField(
            model_name='cup',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2017, 9, 21, 8, 4, 30, 667091, tzinfo=utc)),
        ),
    ]
