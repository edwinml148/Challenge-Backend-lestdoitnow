from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from inventory.models import Warehouse_admin, Customers
import pdb



class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'password2', 'email', 'first_name', 'last_name')

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        del validated_data['password2']
        user = User.objects.create(**validated_data)

        user.set_password(validated_data['password'])
        user.save()

        return user

class UserSerializer(serializers.ModelSerializer):

    creator = serializers.ReadOnlyField(source='creator.username')

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name')

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        rdata={}
        refresh = self.get_token(self.user)
        token={}
        token['refresh'] = str(refresh)
        token['access'] = str(refresh.access_token)
        # User
        rdata['user_id'] = self.user.id
        rdata['username'] = self.user.username
        rdata['first_name'] = self.user.first_name
        rdata['last_name'] = self.user.last_name
        rdata['is_staff'] = self.user.is_staff
        rdata['is_superuser'] = self.user.is_superuser
        rdata['token'] = token
        try:
            warehouse = Warehouse_admin.objects.get(user_id = self.user.id)
        except:
            theWarehouse = None
        else:
            theWarehouse = warehouse.warehouse_id
        try:
            customer = Customers.objects.get(user_id = self.user.id)
        except:
            theCustomer = None
        else:
            theCustomer = customer.id
        if self.user.is_staff or self.user.is_superuser:
            rdata['warehouse'] = theWarehouse
        else:
            rdata['customer'] = theCustomer

        return rdata


