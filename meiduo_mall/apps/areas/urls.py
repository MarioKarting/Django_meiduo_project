# !/usr/bin/env python
# _*_ coding:utf-8 _*_


from django.conf.urls import url

from . import views

urlpatterns = [
    #    1.获取省市区数据
    url(r'^areas/$', views.AreasView.as_view(), name='area')
]
