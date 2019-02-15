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
from .views import timelineView, categoryView, categoryQueryView

urlpatterns = [
    url(r'^time/$', timelineView.as_view(), name='timeline_page'),
    url(r'^category/$', categoryView.as_view(), name='category_page'),
    url(r'^category_query/(?P<category_id>\d+)/$', categoryQueryView.as_view(), name='category_query'),
]
