# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.views.generic.base import View
from articleApp.views import get_artinfo
from articleApp.models import ArticleModel
from pure_pagination import Paginator, PageNotAnInteger


# Create your views here.


class categoryQueryView(View):
    def get(self, request, category_id):
        result = []
        datas = ArticleModel.objects.filter(article_category=category_id).order_by('-add_time')
        for data in datas:
            result.append(data)
        # 分页功能
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        page_result = Paginator(result, 4, request=request)
        result = page_result.page(page)

        return render(request, 'category_query.html', {
            'category_query': result
        })


class timelineView(View):
    def get(self, request):
        current_page = 'timeline'
        result = get_artinfo(mode='all', art_id='')
        return render(request, 'timeline.html', {
            'archive_msg': result,
            'current_page': current_page,
        })


class categoryView(View):
    def get(self, request):
        current_page = 'category'
        return render(request, 'category.html', {
            'current_page': current_page,
        })
