# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-06 10:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.CharField(max_length=256)),
                ('tid', models.IntegerField()),
                ('out', models.TextField()),
                ('program', models.TextField()),
                ('qno', models.IntegerField()),
                ('language', models.IntegerField()),
            ],
            options={
                'db_table': 'answer',
            },
        ),
        migrations.CreateModel(
            name='prog_ques',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prog', models.TextField()),
                ('pname', models.CharField(max_length=256)),
                ('alotted_time', models.IntegerField()),
                ('qno', models.IntegerField()),
                ('mark', models.IntegerField()),
            ],
            options={
                'db_table': 'prog_ques',
            },
        ),
        migrations.CreateModel(
            name='testcases',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_cases', models.TextField(max_length=100)),
                ('question_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='oncomp.prog_ques')),
            ],
        ),
    ]
