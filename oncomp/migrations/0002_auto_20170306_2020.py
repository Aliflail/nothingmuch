# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-06 20:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oncomp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='testcases',
            name='test_out',
            field=models.TextField(default=b'No Output', max_length=1000),
        ),
        migrations.AlterField(
            model_name='testcases',
            name='test_cases',
            field=models.TextField(max_length=1000),
        ),
    ]
