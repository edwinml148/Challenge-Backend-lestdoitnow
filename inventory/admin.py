from django.contrib import admin

from inventory.models.cities import Cities
from inventory.models.customers import Customers
from inventory.models.products import Products
from inventory.models.warehouses import Warehouses

@admin.register(Cities)
class CityAdmin(admin.ModelAdmin):
    'Cities'
    list_display = (
        'id',
        'name',
        'slug_name',
    )
    search_fields = (
        'id',
        'name',
        'slug_name',
    )

@admin.register(Customers)
class CustomersAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'slug_name',
    )
    search_fields = (
        'id',
        'slug_name',
        'name',
    )
    list_filter = (
        'industry',
        'is_deleted',
        )

@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'perishable',
    )
    search_fields = (
        'sku',
        'ean',
        'name',
    )
    list_filter = (
        'is_deleted',
        'perishable',
        'customer',
        )

@admin.register(Warehouses)
class WarehousesAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'city',
    )
    search_fields = (
        'name',
        'latitude',
        'longitude',
    )
    list_filter = (
        'city',
        'is_deleted',
        )