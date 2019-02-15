# -*- coding: utf-8 -*-

from datetime import datetime
from django.db import models
from blogUserApp.models import BlogAuthorModel

# Create your models here.

class BlogInfoModel(models.Model):
    """
    博客信息设置
    """
    blog_title = models.CharField(max_length=20,verbose_name=u"博客标题")
    blog_author = models.ForeignKey(BlogAuthorModel,verbose_name=u"博主信息")
    blog_desc = models.TextField(max_length=100,verbose_name=u"博客介绍")
    blog_footer = models.CharField(max_length=60, verbose_name=u"博客底部信息")
    blog_support = models.TextField(max_length=50,verbose_name=u"技术支持信息")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"修改时间")

    class Meta:
        verbose_name = u"博客信息管理"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.blog_title





