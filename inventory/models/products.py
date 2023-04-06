from django.db import models
from inventory.models.customers import Customers

class Products(models.Model):
    id = models.AutoField(primary_key=True)
    sku = models.IntegerField(null=True)
    ean = models.BigIntegerField(null=True)
    name = models.CharField(max_length =50, null=False)
    description = models.CharField(max_length =50, null=True)
    perishable = models.BooleanField(default=False, null=False)
    is_deleted = models.BooleanField(default=False, null=False)
    created_at= models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True)
    customer = models.ForeignKey(Customers, on_delete=models.CASCADE, null=False)
    def __str__(self):
        return str(self.sku)
    class Meta:
        verbose_name_plural = 'Products'

    