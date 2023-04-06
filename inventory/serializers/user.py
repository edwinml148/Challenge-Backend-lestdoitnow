from gettext import find
from rest_framework import serializers
from inventory.models import *
from django.contrib.auth.models import User
from .warehouses import WarehouseAdminSerializer
import pdb




class UserSerializer(serializers.ModelSerializer):  # create class to serializer user model
    customer_id = serializers.PrimaryKeyRelatedField(
        source="customers",
        queryset=Customers.objects.all(),
        many=False,
        required=False
    )
    warehouse = WarehouseAdminSerializer(many=False, required = False)
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'customer_id', 'warehouse', 'is_staff', 'is_superuser')
    
    def update(self, instance, validated_data):
        pdb.set_trace()
        return super().update(instance, validated_data)