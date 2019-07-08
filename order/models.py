from django.db import models
from user.models import CustomerUser
from cart.models import Cart
from product.models import Product
# Create your models here.


class Order(models.Model):
    user = models.ForeignKey(CustomerUser, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    shipping_address = models.CharField(max_length=255,default='')
    order_description = models.TextField(default='')
    is_completed = models.BooleanField(default=False)

    #class Meta:
    #    ordering = ('-created',)

    def __str__(self):
        return 'Order {}'.format(self.id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order,
                              related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product,
                                related_name='order_items', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=0)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity
