from django.contrib.auth.models import User
from django.db import models


class Customers(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length =50, null=False)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length =15, null=True)
    industry = models.CharField(max_length =20, null=True)
    is_deleted = models.BooleanField(default=False, null=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    created_at= models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True)
    slug_name = models.SlugField(max_length=4, unique=True)
    def __str__(self):
        return str(self.name)
    class Meta:
        verbose_name_plural = 'Customers'
    def save(self, *args, **kwargs):
         if not self.user:
              self.user = None
         super(Customers, self).save(*args, **kwargs)