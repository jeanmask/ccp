# -*- coding: utf-8 -*-

from decimal import Decimal

from rest_framework import serializers

from .models import Offer, OperationalSystem


class OfferSerializer(serializers.ModelSerializer):
    def to_representation(self, obj):
        data = super(OfferSerializer, self).to_representation(obj)
        if hasattr(obj, 'exchanged_price')\
                and hasattr(obj, 'exchanged_price_currency'):
            exchanged_price = Decimal(obj.exchanged_price)
            exchanged_price = exchanged_price.quantize(Decimal("1.00"))
            data['exchanged_price'] = '{:.2f}'.format(exchanged_price)
            data['exchanged_price_currency'] = obj.exchanged_price_currency
        return data

    class Meta:
        model = Offer
        fields = (
            'id', 'seller', 'cpu_cores', 'memory_size', 'disk_size',
            'disk_type', 'price', 'price_currency', 'operational_systems',
        )
        depth = 1


class OSSerializer(serializers.ModelSerializer):
    class Meta:
        model = OperationalSystem
        fields = ('id', 'name',)
