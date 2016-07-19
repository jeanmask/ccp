# -*- coding: utf-8 -*-

import re

from django.db import models
from django.db.models.expressions import RawSQL
from django.utils.translation import ugettext as _
from djmoney.models.fields import MoneyField
from sizefield.models import FileSizeField
from sizefield.utils import filesizeformat


class OfferQuerySet(models.QuerySet):
    def exchange_currency(self, currency_code):
        """
        Exchange price in queryset to `currency_code`

        :param currency_code: ISO 4217 currency code eg.: `USD`
        :type currency_code: str
        :return: annotated querset
        :rtype: QuerySet
        """

        if not currency_code or not re.match(r'^[A-Z]{3}$', currency_code):
            raise ValueError('Currency "%s" is not valid' % currency_code)

        sql = """(
            offers_offer.price / (
                SELECT djmoney_rates_rate.value FROM djmoney_rates_rate
                WHERE currency = offers_offer.price_currency
                ORDER BY date DESC LIMIT 1
            ) * (
                SELECT value FROM djmoney_rates_rate
                WHERE currency = %s
                ORDER BY date DESC LIMIT 1
            )
        )"""

        params = (currency_code,)

        return self.annotate(
            exchanged_price=RawSQL(sql, params),
            exchanged_price_currency=RawSQL('%s', params)
        )


class OfferManager(models.Manager):
    def get_queryset(self):
        return OfferQuerySet(self.model, using=self._db)


class Offer(models.Model):
    objects = OfferManager()

    seller = models.ForeignKey('sellers.Seller', related_name='offers')

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

    price = MoneyField(
        verbose_name=_('Price'),
        max_digits=10,
        decimal_places=2,
        default_currency='USD',
    )

    def get_cpu_cores_display(self):
        """
        Returns formatted cpu core number

        :returns: Plural or singular formatted cpu core number
        :rtype: str

        .. note::
        eg.: 1 core, 2 cores
        """

        return '%s %s' % (
            self.cpu_cores, _('cores') if self.cpu_cores > 1 else _('core')
        )
    get_cpu_cores_display.short_description = _('CPU')
    get_cpu_cores_display.admin_order_field = 'cpu_cores'

    def get_memory_size_display(self):
        """
        Returns formatted memory size

        :returns: Formatted and converted memory size with unit abbr
        :rtype: str

        .. note::
        eg.: 512MB, 1GB, 8GB
        """
        return filesizeformat(self.memory_size, decimals=0)
    get_memory_size_display.short_description = _('Memory size')
    get_memory_size_display.admin_order_field = 'memory_size'

    def get_disk_size_display(self):
        """
        Returns formatted disk size

        :returns: Formatted and converted disk size with unit abbr
        :rtype: str

        .. note::
        eg.: 512MB, 1GB, 8GB
        """
        return filesizeformat(self.disk_size, decimals=0)
    get_disk_size_display.short_description = _('Disk size')
    get_disk_size_display.admin_order_field = 'disk_size'

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

        return txt % {
            'cores': self.cpu_cores,
            'memory': self.get_memory_size_display(),
            'disk': self.get_disk_size_display(),
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
