# -*- coding: utf-8 -*-

from django.contrib import admin
from ccp.sellers.models import Seller


@admin.register(Seller)
class SellerAdmin(admin.ModelAdmin):
    pass
