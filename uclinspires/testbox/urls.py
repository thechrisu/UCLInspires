__author__ = 'VickyD'

from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns = [
     url(r'^home$', views.index, name='index'),
]
