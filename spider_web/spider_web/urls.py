from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'spider_web.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),
                       url(r'^wechat/', include('wechat.urls')),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^app/', include('app.urls')),
                       )
