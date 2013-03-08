from django.conf.urls.defaults import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'testproj.views.home', name='home'),
    url(r'^stations/$', 'bizi.views.list_stations', name='home'),
    #url(r'^bizi/', include('bizi.urls')),

)
