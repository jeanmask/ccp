# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext as _


class Seller(models.Model):
    """Sellers model"""
    name = models.CharField(
        verbose_name=_('Name'),
        max_length=100,
    )
    homepage = models.URLField(
        verbose_name=_('Homepage'),
        help_text=_('Seller\'s homepage URL'),
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Seller')
        verbose_name_plural = _('Sellers')
        ordering = ('name',)
