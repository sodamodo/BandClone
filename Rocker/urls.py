from django.conf.urls import patterns, include, url
from Rocker import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from BandClone import settings
from django.conf.urls.static import static
urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'Rocker.views.hello', name='hello'),


) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

