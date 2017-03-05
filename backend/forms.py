# -*- coding:utf-8 -*-
# Last-Modified date 2017/3/4

from django.forms import ModelForm
from backend.models import Article, Category


class categoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'nav_status']

