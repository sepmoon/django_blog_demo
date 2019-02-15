# -*- coding: utf-8 -*-

from datetime import datetime
from django.db import models
from django.utils.html import strip_tags
from ckeditor_uploader.fields import RichTextUploadingField
from taggit.managers import TaggableManager


# Create your models here.

# 文章分类
class CategoryModel(models.Model):
    category_name = models.CharField(max_length=100, verbose_name=u"分类")

    class Meta:
        verbose_name = u"分类"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.category_name


# 文章
class ArticleModel(models.Model):
    article_title = models.CharField(max_length=20, verbose_name=u"文章标题")
    article_desc = RichTextUploadingField(default=u"正在添加...", max_length=300, verbose_name=u"文章正文")
    article_excerpt = models.CharField(max_length=200, blank=True, verbose_name=u"文章摘要")
    author_name = models.CharField(max_length=10, verbose_name=u"作者名称")
    article_category = models.ForeignKey(CategoryModel, default='', verbose_name=u"分类")
    article_tags = TaggableManager()
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"文章管理"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.article_title

    # 重写save,自动生成文章摘要
    def save(self, *args, **kwargs):
        if not self.article_excerpt:
            # strip_tags 去掉HTML文本的全部HTML标签,再摘取前54个字符
            self.article_excerpt = strip_tags(self.article_desc)[:80]

        super(ArticleModel, self).save(*args, **kwargs)
