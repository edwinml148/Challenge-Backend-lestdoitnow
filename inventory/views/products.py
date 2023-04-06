from rest_framework.generics import RetrieveUpdateAPIView, ListCreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from django_filters import rest_framework as filters
from rest_framework.filters import OrderingFilter
from inventory.models import *
from inventory.serializers import *
from inventory.pagination import CustomPagination
from inventory.filters import *

#Products
class ListCreateProductGeneralAPIView(ListCreateAPIView):
    serializer_class = ProductsSerializer
    queryset = Products.objects.all().order_by('name').filter(is_deleted=False)
    permission_classes = [IsAuthenticated, IsAdminUser]
    pagination_class = CustomPagination
    filter_backends = (filters.DjangoFilterBackend, OrderingFilter)
    filterset_class = ProductsFilter
    ordering_fields = ('name', 'sku', 'ean', 'perishable',)
    

    def perform_create(self, serializer):
        customer = Customers.objects.get(id = int(self.kwargs['customer']))
        serializer.save(customer = customer)

    def get_queryset(self):
        qs = super().get_queryset() 
        return qs.filter(customer_id=self.kwargs['customer'])
    

class RetrieveUpdateDestroyProductAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = ProductsSerializer
    queryset = Products.objects.all()
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        qs = super().get_queryset() 
        return qs.filter(customer_id=self.kwargs['customer'])

    def perform_destroy(self, serializer):
        #pdb.set_trace()
        serializer.is_deleted = True
        return super().perform_update(serializer)


class ListProductAvailableAPIView(ListAPIView):
    serializer_class = ProductsSerializer
    queryset = Products.objects.all().filter(available__gte = 1).order_by('name').distinct()
    permission_classes = [IsAuthenticated]
    pagination_class = CustomPagination
    filter_backends = (filters.DjangoFilterBackend, OrderingFilter)
    filterset_class = ProductsFilter
    ordering_fields = ('name', 'sku', 'ean', 'perishable',)

    def get_queryset(self):
        qs = super().get_queryset() 
        return qs.filter(customer_id=self.kwargs['customer']).order_by('name')