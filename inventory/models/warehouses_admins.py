from django.db import models
from inventory.models.warehouses import Warehouses
from django.contrib.auth.models import User

class Warehouse_admin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=False, blank=False, primary_key=True )
    warehouse = models.ForeignKey(Warehouses, on_delete=models.CASCADE, null=False, blank=False)
    created_at= models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True)
    def __str__(self):
        return str(self.name)
    class Meta:
        verbose_name_plural = 'Warehouses_Admins'