__author__ = 'MatthewHan'
from django.conf.urls import patterns, url # import functions to match patterns
from apps.interests import views
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^users/', views.users, name = 'users'),
    url(r'^user/(?P<user_id>\d+)/$', views.show, name = 'show'),
]