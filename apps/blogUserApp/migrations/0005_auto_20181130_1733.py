# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-30 17:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogUserApp', '0004_auto_20181130_1727'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogauthormodel',
            name='author_logo',
            field=models.ImageField(blank=True, null=True, upload_to='images/author', verbose_name='博主头像'),
        ),
    ]
