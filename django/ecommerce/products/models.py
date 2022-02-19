from django.db import models


# Create your models here.

class Product(models.Model):
    sku = models.CharField(max_length=15, blank=False, unique=True)
    name = models.CharField(max_length=255, blank=False)
    stock = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0.0)
    category = models.CharField(max_length=100, blank=False)
    image = models.ImageField(
        upload_to='img/product/',
        default='img/product/1.png')
