# -*- coding: utf-8 -*-

from django.conf.urls import url, include
from rest_framework import routers

from .views import SellerViewSet


router = routers.DefaultRouter()
router.register(r'sellers', SellerViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),
]
