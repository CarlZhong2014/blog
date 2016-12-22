# -*- coding: utf-8 -*-
# @Author: CarlZ
# @Date:   2016-12-14 23:35:04
# @Last Modified by:   CarlZ
# @Last Modified time: 2016-12-22 22:52:00
from django.conf.urls import url
from . import views

urlpatterns = [
    # /blog/
    url(r'^$',
        views.blog_home,
        name='blog_home'
        ),
    # /blog/tag/<tag_id>/
    url(r'^tag/(?P<tag_id>\d+)[/]$',
        views.tag_articles,
        name='tag_articles'
        ),
    # /blog/catagory/<catagory_name>/
    url(r'^catagory/(?P<catagory_name>[a-z]+)[/]$',
        views.catagories,
        name='catagories'
        ),
    # /blog/detail/<article_id>/
    url(r'^detail/(?P<article_id>\d+)[/]$',
        views.article_detail,
        name='article_detail'
        ),
    # /blog/catagory/<catagory_name>/<tag_id>/
    url(r'^catagory/(?P<catagory_name>[a-z]+)/(?P<tag_id>\d+)[/]$',
        views.catagories_tags,
        name='catagories_tags'
        ),
]
