# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-10 14:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0002_auto_20160203_1125'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='question_comment',
            field=models.CharField(default='comment is', max_length=200, verbose_name='comment.Comment'),
            preserve_default=False,
        ),
    ]
