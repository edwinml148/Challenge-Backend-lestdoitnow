from gettext import find
from rest_framework import serializers
from inventory.models import *
from django.contrib.auth.models import User
import pdb


class CustomersSerializer(serializers.ModelSerializer):  # create class to serializer model

    user = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        many=False,
        required=False
    )

    class Meta:
        model = Customers
        fields = ('id', 'name', 'email', 'phone_number', 'industry', 'user', 'created_at', 'slug_name')

class CustomerSerializer(serializers.ModelSerializer):  # create class to serializer model

    class Meta:
        model = Customers
        fields = ('id', 'name', 'email', 'phone_number', 'industry', 'user_id', 'created_at', 'slug_name')
        #264686