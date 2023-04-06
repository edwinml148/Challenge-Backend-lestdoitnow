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

#Customers
class ListCreateCustomersAPIView(ListCreateAPIView):
    serializer_class = CustomersSerializer
    queryset = Customers.objects.all().order_by('id').filter(is_deleted=False)
    permission_classes = [IsAuthenticated, IsAdminUser]
    pagination_class = CustomPagination
    filter_backends = (filters.DjangoFilterBackend, OrderingFilter)
    filterset_class = CustomersFilter
    ordering_fields = ('name', 'sku', 'ean', 'perishable',)
    

    def perform_create(self, serializer):
        serializer.save()


class RetrieveUpdateDestroycustomersAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = CustomersSerializer
    queryset = Customers.objects.all()
    permission_classes = [IsAuthenticated, IsAdminUser]

    def perform_destroy(self, serializer):
        #pdb.set_trace()
        serializer.is_deleted = True
        return super().perform_update(serializer)