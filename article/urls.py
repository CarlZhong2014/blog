# -*- coding: utf-8 -*-
# @Author: CarlZ
# @Date:   2016-12-14 23:35:04
# @Last Modified by:   CarlZ
# @Last Modified time: 2016-12-19 23:09:18
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
    # /blog/<catagory_name>/
    url(r'^(?P<catagory_name>[a-z]+)[/]$',
        views.catagories,
        name='catagories'
        ),
    # /blog/<catagory_name>/<tag_id>/
    url(r'^(?P<catagory_name>[a-z]+)/(?P<tag_id>\d+)[/]$',
        views.catagories_tags,
        name='catagories_tags'
        ),
    # /blog/<category_name>/<article_id>/
    url(r'^detail/(?P<article_id>\d+)[/]$',
        views.article_detail,
        name='article_detail'
        ),
]
