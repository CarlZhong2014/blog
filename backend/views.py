# -*- coding:utf-8 -*-
# Last-Modified date 2017/3/4
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.core.exceptions import ObjectDoesNotExist
from backend.models import Article, Category
from backend import forms


# Create your views here.


def create_article(request):
    """
    create new article
    :param request:
    :return: The page for user to typing his/her own article.
    """
    if request.method == "POST":
        title = request.POST.get("title")
        author = request.POST.get("author")
        categoryID = request.POST.get("category")
        topped = request.POST.get("topped")
        status = request.POST.get("status")
        abstract = request.POST.get("abstract")
        content = request.POST.get("content")
        categoryObj = Category.objects.get(pk=categoryID)

        if topped is None:
            topped = False
        else:
            topped = True

        if status is None:
            status = False
        else:
            status = True
        Article.objects.create(title=title,
                               author=author,
                               status=status,
                               topped=topped,
                               abstract=abstract,
                               content=content,
                               category=categoryObj
                               )
        return HttpResponseRedirect(reverse('backend_list_article'))

    else:
        cateList = Category.objects.all()
        return render(request, "create.html", {"categories": cateList})


def list_article(request):
    """
    list all article information from article tables;
    :param request:
    :return:
    """
    articleList = Article.objects.all()
    return render(request, 'list.html', {'item_list': articleList})


def modified_article(request):
    """
    modified a existed article
    :param request:
    :return: The page show the specific article to waiting for user for changes it.
    """
    if request.method == "POST":
        title = request.POST.get("title")
        author = request.POST.get("author")
        categoryID = request.POST.get("category")
        topped = request.POST.get("topped")
        status = request.POST.get("status")
        abstract = request.POST.get("abstract")
        content = request.POST.get("content")
        categoryObj = Category.objects.get(pk=categoryID)

        if topped is None:
            topped = False
        else:
            topped = True

        if status is None:
            status = False
        else:
            status = True

        articlePK = int(request.POST.get("pk"))
        articleInfo = Article.objects.get(pk=articlePK)
        articleInfo.title = title
        articleInfo.author = author
        articleInfo.category = categoryObj
        articleInfo.topped = topped
        articleInfo.status = status
        articleInfo.abstract = abstract
        articleInfo.content = content
        articleInfo.save()
        return HttpResponseRedirect(reverse('backend_list_article'))

    if request.method == "GET":
        articlePK = int(request.GET.get("pk"))
        articleInfo = Article.objects.get(pk=articlePK)
        cateList = Category.objects.all()
        return render(request, "modified.html", {"artInfo": articleInfo, "categories": cateList})


def delete_article(request):
    """
    delete article
    :param request:
    :return: The page of operation result
    """
    if request.method == "GET":
        articlePK = int(request.GET.get("pk"))
        Article.objects.get(pk=articlePK).delete()

    return HttpResponseRedirect(reverse('backend_list_article'))


def list_category(request):
    """
    For list all category
    :param request:
    :return:
    """
    category_list = Category.objects.all()
    return render(request, 'category_list.html', {'item_list': category_list})


def create_category(request):
    """
    create new article
    :param request:
    :return: The page for user to typing his/her own article.
    """
    if request.method == "POST":
        nav_status = request.POST.get("nav_status")
        name = request.POST.get("name")
        if name != "":
            if nav_status == "on":
                nav_status = True
            else:
                nav_status = False
            new_category = Category.objects.create(name=name, nav_status=nav_status)
        return HttpResponseRedirect(reverse('backend_list_category'))
    return render(request, 'category_create.html')


def modified_category(request):
    """
    modified a existed article
    :param request:
    :return: The page show the specific article to waiting for user for changes it.
    """
    # 通过GET方法传递要修改的类别id
    if request.method == "GET":
        PK = int(request.GET.get('id'))
        # 如果id存在，返回一个包含该类别信息的表单页，否则返回不存在页面。
        try:
            modCategory = Category.objects.get(pk=PK)
        except ObjectDoesNotExist:
            return HttpResponse("unable to delete, it's not existed")
        modForm = forms.categoryForm(instance=modCategory)
        return render(request, "category_modified.html", {"form": modForm, "pk": PK})

    # POST 方法用于提交修改信息。
    elif request.method == "POST":
        # pk 值是上面GET方法返回表单中的一个隐藏的<input>,用于确认修改那个类别的信息。
        PK = int(request.POST.get("pk"))
        # 同样判断改类别是否存在
        try:
            modCategory = Category.objects.get(pk=PK)
        except ObjectDoesNotExist:
            return HttpResponse("unable to delete, it's not existed")
        modForm = forms.categoryForm(request.POST, instance=modCategory)
        # 验证数据
        if modForm.is_valid():
            # 保存数据
            modForm.save()
            return render(request, "success.html")
        else:
            return HttpResponse("unable to delete, it's not existed")


def delete_category(request):
    """
    delete article
    :param request:
    :return: The page of operation result
    """
    if request.method == "GET":
        PK = int(request.GET.get("id"))
        try:
            delCategory = Category.objects.get(pk=PK)
        except ObjectDoesNotExist:
            return HttpResponse("unable to delete, it's not existed")
        delCategory.delete()
        return render(request, 'success.html')
    else:
        return HttpResponse("unable to delete, it's not existed")
