from django.db import models
from .products import Products
from .warehouses import Warehouses
from .lot_description import Lot_description

class Products_on_warehouses(models.Model):
    product = models.ForeignKey(Products, related_name='available', on_delete=models.CASCADE, null=False)
    stock = models.PositiveIntegerField(null=False, default=0)
    warehouse = models.ForeignKey(Warehouses, on_delete=models.CASCADE, null=False)
    lot = models.ForeignKey(Lot_description, on_delete=models.CASCADE, null=True)