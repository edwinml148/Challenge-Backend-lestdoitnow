from django.db import models
from .products import Products

class Lot_description(models.Model):
    lot_id = models.CharField(primary_key=True, max_length=20, default="default_lot")
    due_date = models.DateField(auto_now_add=False, auto_now=False, null=True)
    product = models.ForeignKey(Products, on_delete=models.CASCADE, null=False)