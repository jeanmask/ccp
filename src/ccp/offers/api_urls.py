# -*- coding: utf-8 -*-

from django.conf.urls import url, include
from rest_framework import routers

from .views import OfferViewSet, OSViewSet


router = routers.DefaultRouter()
router.register(r'offers', OfferViewSet)
router.register(r'os', OSViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),
]
