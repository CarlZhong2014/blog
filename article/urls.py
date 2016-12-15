# -*- coding: utf-8 -*-
# @Author: CarlZ
# @Date:   2016-12-14 23:35:04
# @Last Modified by:   CarlZ
# @Last Modified time: 2016-12-15 22:54:10
from django.conf.urls import url
from . import views

urlpatterns = [
    # /blog/
    url(r'^$',
        views.blog_home,
        name='blog_home'
        ),
    # /blog/<tag_id>/
    url(r'^(?P<tag_id>\d+)[/]$',
        views.tag_articles,
        name='tag_articles'
        ),
    # /blog/<category_name>/
    url(r'^(?P<category_name>[a-z]+)[/]$',
        views.categories,
        name='categories'
        ),
    # /blog/<category_name>/<article_id>/
    url(r'^(?P<category_name>[a-z]+)/(?P<article_id>\d+)[/]$',
        views.article_detail,
        name='article_detail'
        ),
]
