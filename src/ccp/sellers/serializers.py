# -*- coding: utf-8 -*-

from rest_framework import serializers

from .models import Seller


class SellerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Seller
        fields = ('id', 'name', 'homepage',)
