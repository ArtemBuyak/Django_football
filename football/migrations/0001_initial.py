# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-21 11:27
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ArchiveGame',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goal_first', models.IntegerField(default=0)),
                ('goal_second', models.IntegerField(default=0)),
                ('tour', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Cup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cup_name', models.CharField(max_length=200)),
                ('count_commands', models.IntegerField(default=8)),
                ('prize', models.IntegerField(default=1000)),
                ('date', models.DateTimeField(default=datetime.datetime(2017, 9, 20, 11, 27, 32, 649264, tzinfo=utc))),
            ],
        ),
        migrations.CreateModel(
            name='Lists',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cup', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='football.Cup')),
            ],
        ),
        migrations.CreateModel(
            name='Referee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('second_name', models.CharField(max_length=100)),
                ('age', models.IntegerField(default=25)),
                ('experience', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_name', models.CharField(max_length=200)),
                ('number_of_players', models.IntegerField(default=5)),
                ('team_captain', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Winner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cup', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='football.Cup')),
                ('winner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='football.Team')),
            ],
        ),
        migrations.AddField(
            model_name='lists',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='football.Team'),
        ),
        migrations.AddField(
            model_name='cup',
            name='cup',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='football.Referee'),
        ),
        migrations.AddField(
            model_name='archivegame',
            name='team_first',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='football.Team'),
        ),
        migrations.AddField(
            model_name='archivegame',
            name='tourney',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='football.Cup'),
        ),
    ]