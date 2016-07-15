# -*- coding: utf-8 -*-

from django.contrib import admin
from django.utils.translation import ugettext as _

from .models import Offer, OperationalSystem


@admin.register(Offer)
class OfferAdmin(admin.ModelAdmin):
    list_filter = ('seller__name',)

    list_display = (
        'seller',
        'os',
        'get_cpu_cores_display',
        'get_memory_size_display',
        'get_disk_size_display',
        'price',
    )

    fields = (
        'seller',
        'operational_systems',
        'cpu_cores',
        'memory_size',
        ('disk_size', 'disk_type'),
        'price',
    )

    def get_cpu_cores_display(self, obj):
        return '%s %s' % (
            obj.cpu_cores, _('cores') if obj.cpu_cores > 1 else _('core')
        )
    get_cpu_cores_display.short_description = _('CPU')

    def os(self, obj):
        qs = obj.operational_systems.values_list('name', flat=True)
        return ', '.join(qs)
    os.short_description = _('Operational Systems')

    def queryset(self, request, queryset):
        qs = super(OfferAdmin, self).queryset(request, queryset)
        return qs.select_related('seller', 'operational_systems')


@admin.register(OperationalSystem)
class OperationalSystemAdmin(admin.ModelAdmin):
    pass
