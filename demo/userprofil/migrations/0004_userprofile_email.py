# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-09 12:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofil', '0003_remove_userprofile_user_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='email',
            field=models.EmailField(blank=True, max_length=70, null=True, unique=True),
        ),
    ]
