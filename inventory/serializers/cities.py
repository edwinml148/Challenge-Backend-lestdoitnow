from gettext import find
from numpy import source
from rest_framework import serializers
from inventory.models import *
from django.contrib.auth.models import User
import pdb


class WarehousesForCitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warehouses
        fields = ['id', 'name']

class CitiesSerializer(serializers.ModelSerializer):
    warehouses = WarehousesForCitiesSerializer(many=True, read_only=True, source='warehouses_set')
    #pdb.set_trace()
    class Meta:
        model = Cities
        fields = ('id','name','slug_name', 'warehouses')