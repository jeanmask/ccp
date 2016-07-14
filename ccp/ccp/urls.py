# -*- coding: utf-8 -*-

from django.conf.urls import url, include
from django.contrib import admin

api_urls = [
    url(r'^', include('ccp.sellers.api_urls', namespace='api_sellers')),
]

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(api_urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
