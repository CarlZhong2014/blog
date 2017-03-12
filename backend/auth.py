# -*- coding:utf-8 -*-
# Last-Modified date 2017/3/11

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.urlresolvers import reverse
import blog.settings

def user_login(request):
    """
    用户登陆函数，用户登录后，跳转回登陆前的页面。
    :param request:
    :return:
    """
    print blog.settings.STATICFILES_DIRS
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        redirectUrl = request.POST.get("redirect")
        # 认证用户
        loginUser = auth.authenticate(username=username, password=password)
        # 确认认证结果
        if loginUser is not None:
            auth.login(request, loginUser)
            return HttpResponseRedirect(redirect_to=redirectUrl)
        else:
            return render(request, "login.html", {"redirectUrl": redirectUrl})
    elif request.method == "GET":
        redirectUrl = request.GET.get("redirect")
        if redirectUrl is None:
            redirectUrl = "/backend/"
        return render(request, "login.html", {"redirectUrl": redirectUrl})


def user_logout(request):
    """
    用户登出函数。
    :param request:
    :return:
    """
    auth.logout(request)
    return HttpResponseRedirect(reverse("backend_login"))
