__author__ = 'VickyD'


from django.conf.urls import include, url
from django.contrib import admin
from . import views
urlpatterns = [
    url(r'^accounts/loginuser$', 'users.views.login'),
    url(r'^accounts/auth/', 'users.views.auth_view'),
    url(r'^accounts/logout/', 'users.views.logout_view'),
    url(r'^accounts/loggedin/$', 'users.views.loggedin'),
    url(r'^accounts/invalid/$', 'users.views.invalid_login'),
    url(r'^register', 'users.views.register_user', name="register"),
    url(r'^login$', 'users.views.render_login', name="login"),
    url(r'^show_user/(?P<id>[1-9]+)/$', 'users.views.show_user_profile'),

]



