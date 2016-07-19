# Create your views here.

import django_filters

from rest_framework import viewsets, filters

from .models import Offer, OperationalSystem
from .serializers import OfferSerializer, OSSerializer


class OfferFilter(filters.FilterSet):
    min_cpu_cores = django_filters.NumberFilter(
        name="cpu_cores",
        lookup_expr='gte',
    )
    max_cpu_cores = django_filters.NumberFilter(
        name="cpu_cores",
        lookup_expr='lte',
    )

    min_memory_size = django_filters.NumberFilter(
        name="memory_size",
        lookup_expr='gte',
    )
    max_memory_size = django_filters.NumberFilter(
        name="memory_size",
        lookup_expr='lte',
    )

    min_disk_size = django_filters.NumberFilter(
        name="disk_size",
        lookup_expr='gte',
    )
    max_disk_size = django_filters.NumberFilter(
        name="disk_size",
        lookup_expr='lte',
    )

    class Meta:
        model = Offer
        fields = (
            'min_cpu_cores', 'max_cpu_cores',
            'min_memory_size', 'max_memory_size',
            'min_disk_size', 'max_disk_size',
            'disk_type', 'seller'
        )


class OfferViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer
    filter_class = OfferFilter
    ordering_fields = ('cpu_cores', 'memory_size', 'disk_size', 'price',
                       'exchanged_price')
    ordering = ('exchanged_price',)

    def get_queryset(self):
        qs = super(OfferViewSet, self).get_queryset()

        qs = qs.exchange_currency(
            self.request.GET.get('exchange_currency', 'USD')
        )

        min_price = self.request.GET.get('min_price')
        max_price = self.request.GET.get('max_price')
        if min_price:
            qs = qs.filter(exchanged_price__gte=float(min_price))
        if max_price:
            qs = qs.filter(exchanged_price__lte=float(max_price))

        return qs


class OSViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = OperationalSystem.objects.all()
    serializer_class = OSSerializer
