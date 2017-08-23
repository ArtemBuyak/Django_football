# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-22 08:10
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('football', '0003_auto_20170822_1104'),
    ]

    operations = [
        migrations.AddField(
            model_name='cup',
            name='cup_information',
            field=models.CharField(default='Это будет очень хороший турнир', max_length=500),
        ),
        migrations.AlterField(
            model_name='cup',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2017, 9, 21, 8, 10, 2, 96632, tzinfo=utc)),
        ),
    ]