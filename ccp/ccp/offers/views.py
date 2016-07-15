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

    min_price = django_filters.NumberFilter(
        name="price",
        lookup_expr='gte',
    )
    max_price = django_filters.NumberFilter(
        name="price",
        lookup_expr='lte',
    )

    class Meta:
        model = Offer
        fields = (
            'min_cpu_cores', 'max_cpu_cores',
            'min_memory_size', 'max_memory_size',
            'min_disk_size', 'max_disk_size',
            'min_price', 'max_price',
            'disk_type',
        )


class OfferViewSet(viewsets.ModelViewSet):
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer
    filter_class = OfferFilter


class OSViewSet(viewsets.ModelViewSet):
    queryset = OperationalSystem.objects.all()
    serializer_class = OSSerializer
