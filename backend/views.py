# -*- coding:utf-8 -*-
# Last-Modified date 2017/3/4
from django.shortcuts import render
from django.http import HttpResponse
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
    if request.method == "GET":
        cate_list = Category.objects.all()
        return render(request, "create.html", {"categories": cate_list})


def modified_article(request):
    """
    modified a existed article
    :param request:
    :return: The page show the specific article to waiting for user for changes it.
    """


def delete_article(request):
    """
    delete article
    :param request:
    :return: The page of operation result
    """


def list_category(request):
    """
    For list all category
    :param request:
    :return:
    """
    category_list = Category.objects.all()
    return render(request, 'list.html', {'item_list': category_list})


def create_category(request):
    """
    create new article
    :param request:
    :return: The page for user to typing his/her own article.
    """
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
        return render(request, "modified.html", {"form": modForm, "pk": PK})

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


def delete_category(request, PK):
    """
    delete article
    :param request:
    :return: The page of operation result
    """
    PK = int(PK)
    try:
        delCategory = Category.objects.get(pk=PK)
        delCategory.delete()
        return render(request, 'success.html')
    except ObjectDoesNotExist:
        return HttpResponse("unable to delete, it's not existed")
