from django.contrib.auth.models import User
from django.db import models
from .warehouses import Warehouses
from .customers  import Customers

class Movements(models.Model):
    id = models.AutoField(primary_key=True)
    warehouse = models.ForeignKey(Warehouses, on_delete=models.CASCADE, null=False)
    movement_type = models.CharField(max_length =50, null=False)
    description = models.CharField(max_length =200, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at= models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True)
    remission = models.CharField(max_length =40, null=True)
    customer = models.ForeignKey(Customers, on_delete=models.CASCADE)