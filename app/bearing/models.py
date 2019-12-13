from django.db import models


# Create your models here.
class Product(models.Model):
    title = models.CharField(blank=True, max_length=120)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=1000)
    ingredients = models.TextField(default = 'blank')
    available = models.BooleanField(default = 'True')
