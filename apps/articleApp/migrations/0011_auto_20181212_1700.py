# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-12-12 17:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articleApp', '0010_auto_20181211_0254'),
    ]

    operations = [
        migrations.DeleteModel(
            name='TagsModel',
        ),
        migrations.AddField(
            model_name='articlemodel',
            name='article_excerpt',
            field=models.CharField(blank=True, max_length=200, verbose_name='文章摘要'),
        ),
    ]
