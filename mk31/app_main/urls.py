# -*- coding: utf-8 -*-

from django.conf.urls import url
from . import views

app_name = 'app_main'
urlpatterns = [
    url(r'^$', views.index, name='index'),
]