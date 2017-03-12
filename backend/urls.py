# -*- coding:utf-8 -*-
# Last-Modified date 2017/3/4
from django.conf.urls import url
from backend import views, auth


urlpatterns = [
    url(r'^article/list', views.list_article, name='backend_list_article'),
    url(r'^article/create', views.create_article, name='backend_create_article'),
    url(r'^article/modified', views.modified_article, name='backend_modified_article'),
    url(r'^article/delete', views.delete_article, name='backend_delete_article'),
    url(r'^category/list', views.list_category, name='backend_list_category'),
    url(r'^category/create', views.create_category, name='backend_create_category'),
    url(r'^category/modified', views.modified_category, name='backend_modified_category'),
    url(r'^category/delete', views.delete_category, name='backend_delete_category'),
    url(r'^login', auth.user_login, name="backend_login"),
    url(r'^logout', auth.user_logout, name="backend_logout"),
]