# -*- coding: utf-8 -*-

from rest_framework import serializers

from .models import Offer, OperationalSystem


class OfferSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Offer
        fields = (
            'id', 'cpu_cores', 'memory_size', 'disk_size',
            'disk_type', 'price', 'price_currency',)


class OSSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OperationalSystem
        fields = ('id', 'name',)
