from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from BandClone import settings
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    #url(r'^$', 'BandClone.views.home', name='home'),
    url(r'^$', include('Rocker.urls')),

    url(r'^admin/', include(admin.site.urls)),
)


#STATIC AND MEDIA SERVING TWEAKS
urlpatterns += staticfiles_urlpatterns()
urlpatterns += patterns('',
                        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
                            'document_root': settings.MEDIA_ROOT,
                        }),
)
