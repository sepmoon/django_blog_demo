# -*- coding: utf-8 -*-

import xadmin
from .models import BlogInfoModel


# Register your models here.

class BlogInfoAdmin(object):
    list_display = ['blog_title', 'blog_author', 'blog_desc', 'blog_footer']
    search_fields = ['blog_title', 'blog_author', 'blog_desc', 'blog_footer']
    list_filter = ['blog_title', 'blog_author', 'blog_desc', 'blog_footer']


xadmin.site.register(BlogInfoModel, BlogInfoAdmin)
