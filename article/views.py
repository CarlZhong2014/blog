# -*- coding: utf-8 -*-
from models import Article, Catagory, Tag
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def blog_home(request_obj):
    # 获取导航栏信息。
    nav = Catagory.objects.filter(nav_status=True)

    # 获取所有的文章
    articles_list = Article.objects.order_by('-pubdate')
    # 获取所有的标签
    tags_list = Tag.objects.all()
    # 获取全站阅读量前3的文章
    hot_article_list = Article.objects.order_by('-page_view')[0:4]

    context = {
        "articles_list": articles_list,
        "tags_list": tags_list,
        "hot_article_list": hot_article_list,
        "nav": nav
    }
    return render(request_obj, "home.html", context)


def tag_articles(request_obj):
    pass


def catagories(request_obj, catagory_name):
    # 获取导航栏信息。
    nav = Catagory.objects.filter(nav_status=True)

    # 获取当前分类的ID
    catagory_id = Catagory.objects.get(en_name=catagory_name)
    # 获取当前分类的所有文章。
    articles_list = Article.objects.filter(catagory=catagory_id).order_by("-pubdate")
    # 获取当前分类阅读量前3的文章
    hot_article_list = articles_list.order_by('-page_view')[0:4]

    # 获取当前分类下的标签信息
    tags_list = []
    tags_id_list = []
    tag_info = {
        "id": "",
        "name": "",
        "count": 1
    }
    # 获取当前分类下的文章包含标签
    for tag in articles_list.values_list("tags"):
        tag_id = tag[0]
        tags_id_list.append(tag_id)
    # 标签对应的文章数
    tags_id_set = set(tags_id_list)
    for tag_id in tags_id_set:
        tag_info["id"] = tag_id
        tag_info["count"] = tags_id_list.count(tag_id)
        tag_info["name"] = Tag.objects.get(id=tag_id).name
        tags_list.append(tag_info.copy())

    context = {
        "articles_list": articles_list,
        "tags_list": tags_list,
        "hot_article_list": hot_article_list,
        "nav": nav
    }
    return render(request_obj, "list.html", context)



def catagories_tags(request_obj, category_name, tag_id):
    pass


def article_detail(request_obj, article_id):
    article_detail = Article.objects.get(id=article_id)
    catagories_host_list = Article.objects.filter(catagory=article_detail.catagory).order_by('-page_view')[0:1]
    return HttpResponse("%s,%s" % (article_detail.content, catagories_host_list))
