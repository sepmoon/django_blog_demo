# -*- coding: utf-8 -*-

import xadmin
from .models import ArticleModel, CategoryModel
from taggit.models import Tag


# Register your models here.

class ArticleAdmin(object):
    list_display = ['article_title', 'author_name', 'article_category', 'add_time']
    search_fields = ['article_title', 'author_name', 'article_category', 'add_time']
    list_filter = ['article_title', 'author_name', 'article_category', 'add_time']


class CategoryAdmin(object):
    list_display = ['category_name']
    search_fields = ['category_name']
    list_filter = ['category_name']


class TaggitAdmin(object):
    list_display = ['name', 'slug']
    search_fields = ['name', 'slug']
    list_filter = ['name', 'slug']


xadmin.site.register(ArticleModel, ArticleAdmin)
xadmin.site.register(CategoryModel, CategoryAdmin)
xadmin.site.register(Tag, TaggitAdmin)
