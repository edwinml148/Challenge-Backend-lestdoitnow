from gettext import find
from rest_framework import serializers
from inventory.models import *
from django.contrib.auth.models import User
import pdb

class WarehouseListSerializer(serializers.ListSerializer):

    def to_representation(self, data):
        
        #pdb.set_trace()
        request_user = User.objects.get(id = self.context['request'].user.id)
        if (request_user.is_staff or request_user.is_superuser) and (self.context['request'].GET.get('warehouse_filter')=='true'):
            find_warehouse = Warehouse_admin.objects.get(user_id = self.context['request'].user.id)
            data = data.filter(warehouse_id = find_warehouse.warehouse_id)
            #pdb.set_trace()
            return super(WarehouseListSerializer, self).to_representation(data)
        else:
            data = data.all()
            #pdb.set_trace()
            return super(WarehouseListSerializer, self).to_representation(data)

class ProductsOnWarehousesSerializer(serializers.ModelSerializer):

    due_date = serializers.SlugRelatedField(
        source='lot',
        queryset=Lot_description.objects.all(),
        many = False,
        slug_field='due_date'
        )
    warehouse_name = serializers.SlugRelatedField(
        source='warehouse',
        queryset=Warehouses.objects.all(),
        many = False,
        slug_field='name'
        )
    class Meta:
        model = Products_on_warehouses
        list_serializer_class = WarehouseListSerializer
        fields = ('lot_id', 'warehouse_id', 'warehouse_name', 'stock', 'due_date', 'warehouse_name')

class ProductsSerializer(serializers.ModelSerializer):  # create class to serializer model

    customer = serializers.PrimaryKeyRelatedField(
        source='customer_id',
        read_only = True,
        many = False
    )

    available = ProductsOnWarehousesSerializer(many=True, read_only=True)

    class Meta:
        model = Products
        fields = ('id', 'sku', 'ean', 'name', 'description', 'perishable', 'is_deleted', 'created_at', 'updated_at', 'customer', 'available')
