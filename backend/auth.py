# -*- coding:utf-8 -*-
# Last-Modified date 2017/3/11

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import auth


def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        redirectUrl = request.POST.get("redirect")
        loginUser = auth.authenticate(username=username, password=password)
        if loginUser is not None:
            auth.login(request, loginUser)
            return HttpResponseRedirect(redirect_to=redirectUrl)
        else:
            return render(request, "login.html", {"redirectUrl":redirectUrl})
    elif request.method == "GET":
            redirectUrl = request.GET.get("redirect")
            if redirectUrl is None:
                redirectUrl = "/backend/"
            return render(request, "login.html", {"redirectUrl":redirectUrl})

