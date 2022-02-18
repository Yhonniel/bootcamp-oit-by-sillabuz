from django.db import models

# Create your models here.

class Product(models.Model):
    sku = models.CharField(max_length=15, blank=False, unique=True)
    name = models.CharField(max_length=255, blank=False)
    stock = models.IntegerField(default=0)
