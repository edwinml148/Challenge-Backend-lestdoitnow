from django_filters import rest_framework as filters
from .models import *

class ProductsFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='icontains')
    ean = filters.CharFilter(lookup_expr='exact')
    perishable = filters.CharFilter(lookup_expr='icontains')
    sku = filters.CharFilter(lookup_expr='exact')
    class Meta:
        model = Products
        fields = ['name', 'ean', 'perishable', 'sku']

class CustomersFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='icontains')
    email = filters.CharFilter(lookup_expr='icontains')
    phone_number = filters.CharFilter(lookup_expr='exact')
    industry = filters.CharFilter(lookup_expr='icontains')
    slug_name = filters.CharFilter(lookup_expr='exact')
    user_id = filters.CharFilter(lookup_expr='exact')
    class Meta:
        model = Customers
        fields = ['name', 'email', 'phone_number', 'industry', 'slug_name', 'user_id']

class UsersFilter(filters.FilterSet):
    is_superuser = filters.BooleanFilter(lookup_expr='exact')
    is_staff = filters.BooleanFilter(lookup_expr='exact')
    customers = filters.NumberFilter(lookup_expr='exact')