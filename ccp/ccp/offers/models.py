# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext as _
from djmoney.models.fields import MoneyField
from sizefield.models import FileSizeField


class Offer(models.Model):
    seller = models.ForeignKey('sellers.Seller')

    operational_systems = models.ManyToManyField('offers.OperationalSystem')

    cpu_cores = models.PositiveSmallIntegerField(
        verbose_name=_('CPU Cores'),
    )

    memory_size = FileSizeField(
        verbose_name=_('Memory size'),
        help_text=_('Put values in MB, GB or TB. Eg.: 512MB, 1024MB, 2GB.'),
    )

    disk_size = FileSizeField(
        verbose_name=_('Disk size'),
        help_text=_('Put values in MB, GB or TB. Eg.: 20GB, 40GB, 1TB.'),
    )

    DISK_TYPE_SSD = 'ssd'
    DISK_TYPE_HDD = 'hdd'
    DISK_TYPE_CHOICES = (
        (DISK_TYPE_SSD, _('SSD')),
        (DISK_TYPE_SSD, _('HDD')),
    )
    disk_type = models.CharField(
        verbose_name=_('Disk type'),
        max_length=50,
        choices=DISK_TYPE_CHOICES,
        default=DISK_TYPE_SSD,
    )

    amount = MoneyField(
        verbose_name=_('Price'),
        max_digits=10,
        decimal_places=2,
        default_currency='USD',
    )


class OperationalSystem(models.Model):
    name = models.CharField(
        verbose_name=_('Name'),
        max_length=255,
    )

    class Meta:
        verbose_name = _('Operational System')
        verbose_name_plural = _('Operational Systems')
        ordering = ('name',)
