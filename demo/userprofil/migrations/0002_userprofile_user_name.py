# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-03 12:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofil', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='user_name',
            field=models.CharField(default='sumanth', max_length=200),
            preserve_default=False,
        ),
    ]
