from django.conf.urls.defaults import patterns, include, url
from django.views.generic.simple import direct_to_template
from django.conf import settings
from django.contrib import admin
from bt import views as bt
from bt.feeds import RssSiteNewsFeed, AtomSiteNewsFeed


admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', bt.index),
    (r'^list/$', bt.list_violations),
    url(r'^list/(?P<country>[^/]*)(/(?P<operator>[^/]*))?$', bt.filter_violations, name="filter"),
    (r'^ajax/(?P<country>[^/]*)(/(?P<operator>[^/]*))?$', bt.ajax),
    (r'^add/$', bt.add),
    (r'^view/(?P<id>[0-9]*)$', bt.view),
    (r'^(?P<id>[0-9]*)$', bt.view),
    (r'^rss/$', RssSiteNewsFeed()),
    (r'^atom/$', AtomSiteNewsFeed()),
    (r'^activate/$', bt.activate),
    (r'^confirm/(?P<id>[0-9a-z]*)$', bt.confirm),
    (r'^confirm/(?P<id>[0-9]*)/(?P<name>.*)$', bt.confirm),
    (r'^moderate/$', bt.moderate),
    (r'^lookup/$', bt.lookup),
    (r'^accounts/logout$', 'django.contrib.auth.views.logout', {'next_page' : '/'}),
    (r'^accounts/', include('registration.urls')),
    (r'^comments/', include('django.contrib.comments.urls')),
    (r'^about/$', direct_to_template, {'template': 'nn.html'}),
    (r'^start/$', direct_to_template, {'template': 'start.html'}),
    (r'^contact/$', direct_to_template, {'template': 'about.html'}),
    url(r'^captcha/', include('captcha.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEV_SERVER:
    urlpatterns += patterns('',
        (r'^site_media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_PATH}),
    )
