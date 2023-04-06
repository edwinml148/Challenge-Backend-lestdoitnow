from rest_framework.generics import RetrieveUpdateAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from django_filters import rest_framework as filters
from inventory.models import *
from inventory.serializers import *
from inventory.filters import *
import pdb

#Customers
class ListCreateWarehousesAPIView(ListCreateAPIView):
    serializer_class = WarehousesSerializer
    queryset = Warehouses.objects.all().order_by('id').filter(is_deleted=False)
    permission_classes = [IsAuthenticated]
    filter_backends = (filters.DjangoFilterBackend,)
    
    def perform_create(self, serializer):
        city = Cities.objects.get(id = int(self.kwargs['city']))
        serializer.save(city = city)

    def get_queryset(self):
        qs = super().get_queryset() 
        return qs.filter(city_id=self.kwargs['city'])


class RetrieveUpdateWarehouseAPIView(RetrieveUpdateAPIView):
    serializer_class = WarehousesSerializer
    queryset = Warehouses.objects.all()
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        qs = super().get_queryset() 
        return qs.filter(city_id=self.kwargs['city'])

class ListCreateWarehouseAdminsAPIView(ListCreateAPIView):
    serializer_class = WarehouseAdminSerializer
    queryset = Warehouse_admin.objects.all().order_by('warehouse_id')
    permission_classes = [IsAuthenticated]
    filter_backends = (filters.DjangoFilterBackend,)
    
    def perform_create(self, serializer):
        #pdb.set_trace()
        user = User.objects.get(id = int(self.request.data['user']))
        serializer.save(user = user)

class RetrieveUpdateDestroyWarehouseAdminAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = WarehouseAdminSerializer
    queryset = Warehouse_admin.objects.all()
    permission_classes = [IsAuthenticated]

