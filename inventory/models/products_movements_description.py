from django.contrib.auth.models import User
from django.db import models
from .products import Products
from .products_movements import Movements
from .lot_description import Lot_description

class Movements_description(models.Model):
    movement = models.ForeignKey(Movements, related_name='product_details', on_delete=models.CASCADE, null=False)
    product = models.ForeignKey(Products, on_delete=models.CASCADE, null=False)
    product_qty = models.IntegerField(null=False)
    description = models.CharField(max_length =200, null=True)
    lot = models.ForeignKey(Lot_description, on_delete=models.CASCADE, null=True)