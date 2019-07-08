from django.db import models
from product.models import Variation
from user.models import CustomerUser
# Create your models here.
class Category(models.Model):
    title = models.CharField(default='',max_length=100)
    slug = models.CharField(max_length=100,default='')
    description = models.BooleanField(default=True)


class Cart(models.Model):
    user = models.ForeignKey(CustomerUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    item = models.ForeignKey(Variation, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)

    class Product(models.Model):
        title = models.CharField(max_length=255, default='')
        desciption = models.TextField(default='')
        category = models.ForeignKey(Category, on_delete=models.CASCADE)
        price = models.IntegerField(default=0)
        active = models.BooleanField(default=True)

