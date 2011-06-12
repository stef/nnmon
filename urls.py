from django.conf.urls.defaults import patterns, include, url
from django.conf import settings
from django.contrib import admin
from bt import views as bt

admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', bt.index),
    (r'^ajax/(?P<country>[^/]*)(/(?P<operator>[^/]*))?$', bt.ajax),
    (r'^add/$', bt.add),
    (r'^view/(?P<id>[0-9]*)$', bt.view),
    (r'^activate/$', bt.activate),
    (r'^accounts/logout$', 'django.contrib.auth.views.logout', {'next_page' : '/'}),
    (r'^accounts/', include('registration.urls')),
    (r'^comments/', include('django.contrib.comments.urls')),
    url(r'^captcha/', include('captcha.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEV_SERVER:
    urlpatterns += patterns('',
        (r'^site_media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_PATH}),
    )
