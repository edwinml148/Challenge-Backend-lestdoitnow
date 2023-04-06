from django.db import models
from inventory.models.cities import Cities

class Warehouses(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length =50, null=False)
    city = models.ForeignKey(Cities, on_delete=models.CASCADE, null=False)
    address = models.CharField(max_length =50, null=False)
    latitude = models.DecimalField(null=True, max_digits=20, decimal_places = 10)
    longitude = models.DecimalField(null=True, max_digits=20, decimal_places = 10)
    is_deleted = models.BooleanField(default=False, null=False)
    created_at= models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True)
    def __str__(self):
        return str(self.name)
    class Meta:
        verbose_name_plural = 'Warehouses'