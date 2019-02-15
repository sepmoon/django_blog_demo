# -*- coding: utf-8 -*-

from datetime import datetime
from django.db import models


# Create your models here.

class BlogAuthorModel(models.Model):
    """
    博客用户信息设置
    """
    name = models.CharField(max_length=20, verbose_name=u"博主昵称")
    author_logo = models.ImageField(verbose_name=u"博主头像", upload_to="images/author", blank=True, null=True)
    author_desc = models.TextField(max_length=100, verbose_name=u"博主信息")
    author_wechat = models.CharField(max_length=10, verbose_name=u"博主微信")
    author_qq = models.CharField(max_length=10, verbose_name=u"博主QQ")
    author_weibo = models.CharField(max_length=10, verbose_name=u"博主微博")
    author_github = models.CharField(max_length=10, verbose_name=u"博主github")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"修改时间")

    class Meta:
        verbose_name = u"博客用户管理"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
