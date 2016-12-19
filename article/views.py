# -*- coding: utf-8 -*-
from models import Article, Catagory, Tag
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def blog_home(request_obj):
    articles_list = Article.objects.order_by('-pubdate')
    tags_list = Tag.objects.all()
    hot_article_list = Article.objects.order_by('-page_view')[0:4]
    nav = Catagory.objects.filter(nav_status=True)
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
    catagory_id = Catagory.objects.get(en_name=catagory_name)
    articles_list = Article.objects.filter(catagory=catagory_id).order_by("-pubdate")
    hot_article_list = articles_list.order_by('-page_view')[0:4]
    nav = Catagory.objects.filter(nav_status=True)
    tags_list = []
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
    categories_host_list = Article.objects.filter(catagory=article_detail.catagory).order_by('-page_view')[0:1]
    return HttpResponse("%s,%s" % (article_detail.content, categories_host_list))
