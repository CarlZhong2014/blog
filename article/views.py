# -*- coding: utf-8 -*-
from backend.models import Article, Category
from django.shortcuts import render
import json
from django.core.urlresolvers import reverse
from django.http import HttpResponse
import markdown


# Create your views here.


def home(request):
    homeUrl = reverse("article_home")
    allCategory = Category.objects.all()
    categoryNameList = []
    for cateItem in allCategory:
        link = "./category/" + str(cateItem.id)
        categoryNameList.append({"name": cateItem.name, "link": link})
    articleList = Article.objects.filter(status=True)
    return render(request, "home.html", {"categoryArray": json.dumps(categoryNameList), "articles": articleList,
                                         "homeUrl": homeUrl})


def blog_post(request):
    if request.method == "GET":
        id = int(request.GET.get("id"))
    else:
        id = int(request.POST.get("id"))
    articleInfo = Article.objects.get(pk=id)
    allCategory = Category.objects.all()
    categoryNameList = []
    homeUrl = reverse("article_home")
    for cateItem in allCategory:
        link = homeUrl + "category/" + str(cateItem.id)
        categoryNameList.append({"name": cateItem.name, "link": link})
    articleContent = markdown.markdown(articleInfo.content, extensions=['markdown.extensions.extra',
                                                                        'markdown.extensions.codehilite'])
    articleInfo.content = articleContent
    return render(request, "post.html", {"article": articleInfo, "categoryArray": json.dumps(categoryNameList)})


def blog_category_list(request, cid):
    allCategory = Category.objects.all()
    categoryNameList = []
    homeUrl = reverse("article_home")
    for cateItem in allCategory:
        link = homeUrl + "category/" + str(cateItem.id)
        categoryNameList.append({"name": cateItem.name, "link": link})
    categoryRecord = Category.objects.get(pk=int(cid))
    articleList = categoryRecord.article_set.all()
    return render(request, "home.html", {"categoryArray": json.dumps(categoryNameList), "articles": articleList,
                                         "homeUrl": homeUrl})
