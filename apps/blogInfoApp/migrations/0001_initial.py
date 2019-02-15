# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-20 17:13
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('blogUserApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogInfoModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_title', models.CharField(max_length=20, verbose_name='博客标题')),
                ('blog_desc', models.TextField(max_length=100, verbose_name='博客介绍')),
                ('blog_footer', models.CharField(max_length=60, verbose_name='博客底部信息')),
                ('blog_support', models.TextField(max_length=50, verbose_name='技术支持信息')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='修改时间')),
                ('blog_author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogUserApp.BlogAuthorModel', verbose_name='博主信息')),
            ],
        ),
    ]