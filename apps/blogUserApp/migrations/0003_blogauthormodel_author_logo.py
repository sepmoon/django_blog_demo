# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-30 16:56
from __future__ import unicode_literals

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogUserApp', '0002_auto_20181120_1718'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogauthormodel',
            name='author_logo',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
    ]
