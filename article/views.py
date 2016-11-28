# -*- coding: utf-8 -*-
from models import Article
from django.shortcuts import render
# Create your views here.


def blog_index(req):
    article_list = Article.objects.all()
    return render(req, "index.html", {"article_list": article_list})


def detail(req, article_id):
    article_obj = Article.objects.filter(id=article_id)[0]
    article_list = Article.objects.all()
    return render(req, "show.html", {"article_obj": article_obj,"article_list": article_list})
