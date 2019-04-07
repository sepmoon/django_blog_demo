# -*- coding: utf-8 -*-

from django.views.generic.base import View
from django.shortcuts import render
from django.http import HttpResponseNotFound
from CacheFun.blog_cache import get_articles, get_all_articles, get_art_id, get_tag_search
from django.db.models import Q
from .models import ArticleModel
from blogtagsApp.templatetags.blog_tags import get_tags
from pure_pagination import Paginator, PageNotAnInteger


# Create your views here.

# tag cloud 视图
class TagsListView(View):
    def get(self, request, tags_id):
        result = get_tag_search(tags_id)
        tags_result = ''

        # 在缓存中取tags的名称
        tags_list = get_tags()
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
        results = get_all_articles()

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
        art_data = get_articles(art_id)

        # 上一篇和下一篇按钮,到顶部或者到底部的判断.
        left_top = False
        right_top = False

        # 判断文章id在结果中的位置排位
        id_list = get_art_id()
        try:
            list_position = id_list.index(int(art_id))
        except ValueError:
            search_response = HttpResponseNotFound(charset='gb2312')
            search_response.content = '<h1>没有相关文章内容，请重新输入。</h1>'
            return search_response
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
