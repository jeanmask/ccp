# -*- coding: utf-8 -*-

from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class SellersConfig(AppConfig):
    name = 'ccp.sellers'
    verbose_name = _('Sellers')
