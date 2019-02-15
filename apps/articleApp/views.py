# -*- coding: utf-8 -*-

from django.views.generic.base import View
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseNotFound
from django.core.cache import cache
from django.db.models import Q
from .models import ArticleModel
from blogtagsApp.templatetags.blog_tags import get_tags
from pure_pagination import Paginator, PageNotAnInteger


# Create your views here.


# 提取文章内容
def get_artinfo(mode, art_id):
    # 文章单页部分信息提取
    if mode == 'filter':
        key = 'art-{}'.format(art_id)
        if key in cache:
            art_data = cache.get(key)
            return art_data
        else:
            art_data = get_object_or_404(ArticleModel, id=art_id)
            cache.set(key, art_data, 5 * 60)
            return art_data

    # 首页文章信息列表全部提取
    elif mode == 'all':
        key = 'artlist_all'
        if key in cache:
            art_list_all = cache.get(key)
        else:
            art_list_all = []
            art_content = ArticleModel.objects.all().order_by('-add_time')
            if art_content:
                for content in art_content:
                    art_list_all.append(content)
                cache.set(key, art_list_all, 5 * 60)
        return art_list_all

    else:
        pass


# 提取文章id列表
def get_art_id():
    id_list = []
    key = 'artid_all'
    if key in cache:
        id_list = cache.get(key)
    else:
        results = ArticleModel.objects.all()
        if results:
            for result in results:
                id_list.append(result.id)
            cache.set(key, id_list, 5 * 60)
    return id_list


# tag cloud 视图
class TagsListView(View):
    def get(self, request, tags_id):
        key = 'tag_search-{}'.format(tags_id)
        tags_list = ''
        tags_result = ''
        if key in cache:
            result = cache.get(key)
        else:
            result = ArticleModel.objects.filter(article_tags__exact=tags_id).order_by('-add_time')
            if result:
                cache.set(key, result, 5 * 60)

        # 在缓存中取tags的名称
        get_tags_name = False
        while get_tags_name == False:
            tags_list = cache.get('tagsName_list')
            if tags_list:
                get_tags_name = True
            else:
                # 没缓存则建立缓存
                get_tags()
        for tags in tags_list:
            if tags.id == int(tags_id):
                tags_result = tags

        # 分页功能
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        page_result = Paginator(result, 4, request=request)
        result = page_result.page(page)

        return render(request, 'tags_query.html', {
            'tag_search': result,
            'tag_msg': tags_result,
        })


# 搜索结果视图
class SearchView(View):
    def get(self, request):
        search_q = request.GET.get('search_q')
        search_response = HttpResponseNotFound(charset='gb2312')
        if search_q:
            result = ArticleModel.objects.filter(
                Q(article_title__icontains=search_q) | Q(article_desc__icontains=search_q)).order_by('-add_time')
            if result:
                # 分页功能
                try:
                    page = request.GET.get('page', 1)
                except PageNotAnInteger:
                    page = 1
                page_result = Paginator(result, 4, request=request)
                result = page_result.page(page)

                return render(request, 'search_result.html', {
                    'search_msg': result,
                    'search_q': str(search_q),
                })
            else:
                search_response.content = '<h1>搜索不到相关内容，请重新输入。</h1>'
                return search_response
        else:
            search_response.content = '<h1>搜索输入为空，请重新输入。</h1>'
            return search_response


# 首页视图
class IndexView(View):
    def get(self, request):
        current_page = 'home'
        results = get_artinfo(mode='all', art_id='')

        # 分页功能
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        page_result = Paginator(results, 4, request=request)
        result = page_result.page(page)

        return render(request, 'index.html', {
            'index_msg': result,
            'current_page': current_page
        })


# 单页视图
class ArticleView(View):
    def get(self, request, art_id):
        mode = 'filter'
        art_data = get_artinfo(mode, art_id)

        # 上一篇和下一篇按钮,到顶部或者到底部的判断.
        left_top = False
        right_top = False

        # 判断文章id在结果中的位置排位
        id_list = get_art_id()
        list_position = id_list.index(int(art_id))
        try:
            # 到顶部设置left_top为True
            if list_position - 1 == -1:
                left_id = id_list[list_position]
                left_top = True
            else:
                left_id = id_list[list_position - 1]
            right_id = id_list[list_position + 1]
            art_position = {'left_id': left_id, 'right_id': right_id}
        except IndexError:
            # 到底部设置right_top为True
            right_id = id_list[list_position]
            left_id = id_list[list_position - 1]
            art_position = {'left_id': left_id, 'right_id': right_id}
            right_top = True

        return render(request, 'article.html', {
            'art_msg': art_data,
            'id_position': art_position,
            'left_top': left_top,
            'right_top': right_top,
        })
