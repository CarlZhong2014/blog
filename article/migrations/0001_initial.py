# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-12-15 15:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40, verbose_name='\u6807\u9898')),
                ('author', models.CharField(max_length=40, verbose_name='\u4f5c\u8005')),
                ('pubdate', models.DateTimeField(auto_now_add=True, verbose_name='\u53d1\u5e03\u65f6\u95f4')),
                ('content', models.TextField(verbose_name='\u6b63\u6587')),
                ('page_view', models.BigIntegerField(default=0, verbose_name='\u8bbf\u95ee\u91cf')),
            ],
        ),
        migrations.CreateModel(
            name='Catagory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='\u7c7b\u522b\u540d\u79f0')),
                ('symbol', models.CharField(max_length=40, unique=True, verbose_name='\u7c7b\u522b\u6807\u8bc6')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='\u6807\u7b7e\u540d\u79f0')),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='catagory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='article.Catagory', verbose_name='\u5206\u7c7b'),
        ),
        migrations.AddField(
            model_name='article',
            name='tags',
            field=models.ManyToManyField(to='article.Tag', verbose_name='\u6807\u7b7e'),
        ),
    ]
