# -*- coding: utf-8 -*-

import xadmin
from .models import BlogAuthorModel


# Register your models here.

class BlogAuthorAdmin(object):
    list_display = ['name', 'author_wechat', 'author_qq', 'author_weibo', 'author_github']
    search_fields = ['name', 'author_wechat', 'author_qq', 'author_weibo', 'author_github']
    list_filter = ['name', 'author_wechat', 'author_qq', 'author_weibo', 'author_github']


xadmin.site.register(BlogAuthorModel, BlogAuthorAdmin)
