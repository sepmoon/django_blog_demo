#! /usr/bin/env python
# -*- coding: utf-8 -*-

from articleApp.models import ArticleModel
from django.core.cache import cache


# 设置缓存
def StringCache(news):
    def pwrap(fun):
        def wrap(id='', *args, **kwargs):
            key = news + str(id)
            if key in cache:
                _data = cache.get(key)
            else:
                if id == '':
                    _data = fun()
                else:
                    _data = fun(id)
                cache.set(key, _data, 5 * 60)
            return _data

        return wrap

    return pwrap


# 提取指定文章的内容
@StringCache('art')
def get_articles(art_id):
    # art_data = get_object_or_404(ArticleModel, id=art_id)
    try:
        art_data = ArticleModel.objects.get(id=art_id)
    except:
        art_data = {}
    return art_data


# 拿指定tag的数据
@StringCache('tag_search')
def get_tag_search(tags_id):
    result = ArticleModel.objects.filter(article_tags__exact=tags_id).order_by('-add_time')
    return result


# 提取全部文章列表
@StringCache('artlist_all')
def get_all_articles():
    art_list_all = []
    art_content = ArticleModel.objects.all().order_by('-add_time')
    if art_content:
        for content in art_content:
            art_list_all.append(content)
    return art_list_all


# 提取文章id列表
@StringCache('artid_all')
def get_art_id():
    id_list = []
    results = ArticleModel.objects.all()
    if results:
        for result in results:
            id_list.append(result.id)
    return id_list
