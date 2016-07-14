# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext as _
from djmoney.models.fields import MoneyField


class Offer(models.Model):
    seller = models.ForeignKey('sellers.seller')
    cpu_cores = models.PositiveSmallIntegerField(
        verbose_name=_('CPU Cores'),
    )
    memory_size = models.PositiveSmallIntegerField(
        verbose_name=_('Memory size'),
        help_text=_('Put values in MB, eg.: 512, 1024...'),
    )
    disk_size = models.PositiveSmallIntegerField(
        verbose_name=_('Disk size'),
        help_text=_('Put values in GB, eg.: 20, 40...'),
    )
    amount = MoneyField(
        verbose_name=_('Price'),
        max_digits=10,
        decimal_places=2,
        default_currency='USD',
    )
