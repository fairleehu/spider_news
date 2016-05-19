from django.conf.urls import patterns, include, url
from wechat import views

urlpatterns = patterns('',
                       url(r'^$', views.main, name='main'),
                       url(r'^index/$', views.index, name='index'),
                       url(r'^create_menu/$', views.create_menu,
                           name='create_menu'),
                       )
