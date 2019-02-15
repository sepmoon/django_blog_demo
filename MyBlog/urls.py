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

# from django.contrib import admin
from django.conf.urls import url, include
import xadmin
from django.views.static import serve
from MyBlog.settings import MEDIA_ROOT

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^admin/', xadmin.site.urls),
    # 首页
    url(r'^', include('articleApp.urls', namespace='index')),
    # 文章详情页
    url(r'^article/', include('articleApp.urls', namespace='art')),
    # 分类和存档栏目
    url(r'^archive/', include('timelineApp.urls',namespace='time')),

    # media
    url(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),
    # 富文本
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),

]
