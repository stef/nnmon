from django.conf.urls.defaults import patterns, include, url
from django.conf import settings
from bt import views as bt

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    (r'^accounts/logout$', 'django.contrib.auth.views.logout', {'next_page' : '/'}),
    (r'^accounts/', include('registration.urls')),
    (r'^ajax/(?P<country>[^/]*)(/(?P<operator>[^/]*))?$', bt.ajax),
    (r'^add/$', bt.add),
)

if settings.DEV_SERVER:
    urlpatterns += patterns('',
        (r'^site_media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_PATH}),
    )
