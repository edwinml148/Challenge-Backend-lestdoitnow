from gettext import find
from numpy import source
from rest_framework import serializers
from inventory.models import *
from django.contrib.auth.models import User
import pdb

class WarehousesSerializer(serializers.ModelSerializer):
    city = serializers.PrimaryKeyRelatedField(
        source='city_id',
        read_only = True,
        many = False
    )
    class Meta:
        model = Warehouses
        fields = ('id','name', 'name', 'address', 'latitude', 'longitude', 'city')


class WarehouseAdminSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        many = False
    )
    warehouse = serializers.PrimaryKeyRelatedField(
        queryset=Warehouses.objects.all(),
        many=False
    )
    class Meta:
        model = Warehouse_admin
        fields = ('user','warehouse')