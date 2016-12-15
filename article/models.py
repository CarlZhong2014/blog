# -*- coding: utf-8 -*-
# @Author: CarlZ
# @Date:   2016-11-16 00:32:03
# @Last Modified by:   CarlZ
# @Last Modified time: 2016-12-15 23:38:56
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Catagory(models.Model):
    """
        分类
    """
    name = models.CharField('类别名称', max_length=20)
    symbol = models.CharField('类别标识', max_length=40, unique=True)

    def __unicode__(self):
        return self.name


class Tag(models.Model):
    """
        标签
    """
    name = models.CharField('标签名称', max_length=20)

    def __unicode__(self):
        return self.name


class Article(models.Model):
    """
        文章
    """
    title = models.CharField('标题', max_length=40)
    author = models.CharField('作者', max_length=40)
    pubdate = models.DateTimeField('发布时间', auto_now_add=True)
    catagory = models.ForeignKey(Catagory, verbose_name='分类')
    tags = models.ManyToManyField(Tag, verbose_name='标签')
    content = models.TextField('正文')
    page_view = models.BigIntegerField('访问量', default=0)

    def __unicode__(self):
        return self.title
