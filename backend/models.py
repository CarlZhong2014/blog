# -*- coding: utf-8 -*-
# @Author: CarlZ
# @Date:   2016-11-16 00:32:03
# @Last Modified by:   CarlZ
# @Last Modified time: 2016-12-22 22:12:13
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Category(models.Model):
    """
        分类
    """
    name = models.CharField('类别名称', max_length=20)
    nav_status = models.BooleanField('导航项', default=True)

    def __unicode__(self):
        return self.name


class Article(models.Model):
    """
        文章
    """
    title = models.CharField(u'标题', max_length=40)
    author = models.CharField(u'作者', max_length=40)
    create_date = models.DateTimeField(u'创建时间', auto_now_add=True)
    last_modified_date = models.DateTimeField(u'最新修改时间', auto_now=True)
    # 文章状态有两种，一种是草稿（False）、一种是发布（True）。
    status = models.BooleanField(u'文章状态', default=False)
    category = models.ForeignKey(Category, verbose_name=u'分类')
    abstract = models.TextField(u'摘要', max_length=250)
    content = models.TextField(u'正文')
    views = models.BigIntegerField(u'访问量', default=0)
    topped = models.BooleanField(u'置顶', default=False)

    def __unicode__(self):
        return self.title
