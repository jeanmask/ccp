# -*- coding: utf-8 -*-

from django.utils.translation import ugettext as _
from djmoney_rates.exceptions import CurrencyConversionException
from djmoney_rates.utils import convert_money
from rest_framework import serializers

from .models import Offer, OperationalSystem


class OfferSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        self.exchange_currency = kwargs.pop('exchange_currency', None)
        super(OfferSerializer, self).__init__(*args, **kwargs)

    def to_representation(self, obj):
        data = super(OfferSerializer, self).to_representation(obj)
        if self.exchange_currency\
                and self.exchange_currency != obj.price.currency.code:
            try:
                exchanged = convert_money(
                    obj.price.amount,
                    obj.price.currency.code,
                    self.exchange_currency)
                data['exchanged_price'] = exchanged.amount
                data['exchanged_price_currency'] = exchanged.currency.code
            except CurrencyConversionException:
                err = _('Exchange currency "%s" is not valid')
                raise serializers.ValidationError(err % self.exchange_currency)
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
