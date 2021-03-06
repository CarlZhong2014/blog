# -*- coding: utf-8 -*-
# @Author: CarlZ
# @Date:   2016-12-14 23:35:04
# @Last Modified by:   CarlZ
# @Last Modified time: 2016-12-30 00:27:32
from django.conf.urls import url
from article import views

urlpatterns = [
    url(r"^$", views.home, name="article_home"),
    url(r"^article$", views.blog_post, name="article_blog_post"),
    url(r"^category/(?P<cid>\d+)[/]", views.blog_category_list, name="blog_category_list")
]
