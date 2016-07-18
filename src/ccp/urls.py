# -*- coding: utf-8 -*-

from django.conf.urls import url, include, patterns
from django.contrib import admin
from django.conf import settings

api_urls = [
    url(r'^', include('ccp.sellers.api_urls', namespace='api_sellers')),
    url(r'^', include('ccp.offers.api_urls', namespace='api_offers')),
    url(r'^auth/', include('rest_framework.urls', namespace='rest_framework')),
]

urlpatterns = [
    # url(r'^$', TemplateView.as_view(template_name="ccp/home.html")),
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(api_urls)),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    # Providing index.html in development
    urlpatterns += patterns(
        'django.contrib.staticfiles.views',
        url(r'^(?:index.html)?$', 'serve', kwargs={'path': 'index.html'}))
