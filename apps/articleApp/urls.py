"""MyBlog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
# -*- coding: utf-8 -*-

from django.conf.urls import url
from .views import ArticleView, IndexView, SearchView, TagsListView

urlpatterns = [
    url(r'^page/(?P<art_id>\d+)/$', ArticleView.as_view(), name='article_page'),
    url(r'^search/$', SearchView.as_view(), name='search_page'),
    url(r'^tags/(?P<tags_id>\d+)$', TagsListView.as_view(), name='tags_page'),
    url(r'^$', IndexView.as_view(), name='home_page'),
]
