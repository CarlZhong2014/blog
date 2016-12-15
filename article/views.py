# -*- coding: utf-8 -*-
from models import Article, Catagory, Tag
from django.shortcuts import render
# Create your views here.


def blog_home(request_obj):
    articles_list = Article.objects.all()
    tags_list = Tag.objects.all()
    context = {
        "articles_list": articles_list,
        "tags_list": tags_list,
    }
    return render(request_obj, "home.html", context)


def tag_articles(request_obj):
    pass


def categories(request_obj):
    pass

def article_detail(request_obj):
    pass
