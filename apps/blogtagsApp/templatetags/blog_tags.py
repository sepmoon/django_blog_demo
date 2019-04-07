# -*- coding: utf-8 -*-
# 博客基础信息的自定义标签

from django import template
from django.db.models.aggregates import Count
from blogInfoApp.models import BlogInfoModel
from articleApp.models import ArticleModel, CategoryModel
from CacheFun.blog_cache import StringCache
from taggit.models import Tag

register = template.Library()


# 提取博客基础信息
@StringCache('blog_info')
def get_blog_info(num=1):
    # 查询基础信息是否有缓存
    result = ''
    datas = BlogInfoModel.objects.filter(id=num)
    if datas:
        for data in datas:
            result = data
    return result


# 博客标题
@register.simple_tag
def get_blog_title():
    blog_info = get_blog_info()
    return blog_info.blog_title


# 博客描述
@register.simple_tag
def get_blog_desc():
    blog_info = get_blog_info()
    return blog_info.blog_desc


# 博客底部
@register.simple_tag
def get_blog_footer():
    blog_info = get_blog_info()
    return blog_info.blog_footer


# 作者头像
@register.simple_tag
def get_author_logo():
    blog_info = get_blog_info()
    return blog_info.blog_author.author_logo


# 作者名称
@register.simple_tag
def get_author_name():
    blog_info = get_blog_info()
    return blog_info.blog_author.name


# 作者描述
@register.simple_tag
def get_author_desc():
    blog_info = get_blog_info()
    return blog_info.blog_author.author_desc


# 存档栏目查询文章日期
@register.simple_tag
def get_archives():
    return ArticleModel.objects.dates('add_time', 'month', order='DESC')


# 查询分类的栏目和栏目文章的数量统计
@register.simple_tag
def get_category():
    return CategoryModel.objects.annotate(num_posts=Count('articlemodel'))


# 首页标签栏目
@StringCache('tagsName_list')
@register.simple_tag
def get_tags():
    result = Tag.objects.all()
    return result
