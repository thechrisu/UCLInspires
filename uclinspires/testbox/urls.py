__author__ = 'VickyD'

from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns = [
     url(r'^home$', views.index, name='index'),
     url(r'^landingpage$', views.home),
     url(r'^show/(?P<id>[1-9]+)/$', views.show_all_profiles),
]
