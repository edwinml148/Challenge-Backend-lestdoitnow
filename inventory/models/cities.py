from django.db import models

class Cities(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length =50, null=False)
    slug_name = models.SlugField(max_length=3, unique=True)
    created_at= models.DateTimeField(auto_now_add=True, auto_now=False)
    class Meta:
        verbose_name_plural = 'Cities'