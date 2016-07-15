# -*- coding: utf-8 -*-

from functools import partial

from django.db import models
from django.utils.translation import ugettext as _
from djmoney.models.fields import MoneyField
from sizefield.models import FileSizeField
from sizefield.utils import filesizeformat


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

    def __str__(self):
        if self.cpu_cores > 1:
            txt = '%s - %s - %s %s' % (
                _('%(cores)d cores'),
                _('%(memory)s RAM'),
                '%(disk)s',
                _('%(disk_type)s Disk'),
            )
        else:
            txt = '%s - %s - %s %s' % (
                _('%(cores)d core'),
                _('%(memory)s RAM'),
                '%(disk)s',
                _('%(disk_type)s Disk'),
            )

        filesizeformat_ = partial(filesizeformat, decimals=0)

        return txt % {
            'cores': self.cpu_cores,
            'memory': filesizeformat_(self.memory_size),
            'disk': filesizeformat_(self.disk_size),
            'disk_type': self.get_disk_type_display(),
        }

    class Meta:
        verbose_name = _('Offer')
        verbose_name_plural = _('Offers')
        ordering = ('seller_id',)


class OperationalSystem(models.Model):
    name = models.CharField(
        verbose_name=_('Name'),
        max_length=255,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Operational System')
        verbose_name_plural = _('Operational Systems')
        ordering = ('name',)
