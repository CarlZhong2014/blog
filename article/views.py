# -*- coding: utf-8 -*-
from backend.models import Article, Category
from django.shortcuts import render
import json
from django.http import HttpResponse


# Create your views here.


def home(request):
    categoryList = Category.objects.all()
    articleList = Article.objects.all()
    return render(request, "home.html", {"categories": categoryList, "articles": articleList})


def blog_post(request):
    if request.method == "GET":
        id = int(request.GET.get("id"))
    else:
        id = int(request.POST.get("id"))
    articleInfo = Article.objects.get(pk=id)
    categoryList = Category.objects.all()
    categoryNameList = []
    for cats in categoryList:
        categoryNameList.append(cats.name)
    return render(request, "post.html", {"article": articleInfo, "categories": json.dumps(categoryNameList)})
