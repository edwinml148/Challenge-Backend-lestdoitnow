from rest_framework.generics import RetrieveUpdateAPIView, ListCreateAPIView, ListAPIView
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

#Users
class ListUsersApiView(ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all().order_by('id')
    permission_classes = [IsAuthenticated, IsAdminUser]
    filter_backends = (filters.DjangoFilterBackend, OrderingFilter)
    filterset_class = UsersFilter
    ordering_fields = ('id', 'name', 'email', 'perishable',)

class RetrieveUpdateUserAPIView(RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all().order_by('id')
    permission_classes = [IsAuthenticated, IsAdminUser]