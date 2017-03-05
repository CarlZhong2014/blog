# -*- coding:utf-8 -*-
# Last-Modified date 2017/3/4
from django.conf.urls import url
import backend.views

urlpatterns = [
    url(r'^article/create', backend.views.create_article, name='backend_create_article'),
    url(r'^article/modified', backend.views.modified_article, name='backend_modified_article'),
    url(r'^article/delete', backend.views.delete_article, name='backend_delete_article'),
    url(r'^category/list', backend.views.list_category, name='backend_list_category'),
    url(r'^category/create', backend.views.create_category, name='backend_create_category'),
    url(r'^category/modified', backend.views.modified_category, name='backend_modified_category'),
    url(r'^category/(?P<PK>\d+)/delete', backend.views.delete_category, name='backend_delete_category'),
]