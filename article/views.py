# -*- coding: utf-8 -*-
from backend.models import Article, Category
from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


def home(request):
    navList = Category.objects.filter(nav_status=True)
    articleList = Article.objects.all()
    return render(request, "home.html", {"navList": navList, "articles": articleList})
