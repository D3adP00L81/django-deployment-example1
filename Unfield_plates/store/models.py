from django.db import models
from account.models import Customer
from django.utils import timezone

# Create your models here.
class Order(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    date_ordered = models.DateTimeField(default=timezone.now())
    complete = models.BooleanField(default=False)

class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    order = models.ForeignKey(Order,on_delete=models.CASCADE)
    address = models.TextField()
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=50)
    date_added = models.DateTimeField(default=timezone.now())

class Product(models.Model):
    name = models.CharField(max_length=300)
    price = models.IntegerField()
    discount = models.IntegerField(null=True)
    category_1 = models.CharField(max_length=200,null=True)
    category_2 = models.CharField(max_length=200,null=True)
    category_3 = models.CharField(max_length=200,null=True)
    category_4 = models.CharField(max_length=200,null=True)
    category_5 = models.CharField(max_length=200,null=True)
    color = models.CharField(max_length=300,null=True)
    last_price = models.IntegerField(null=True)

    def get_discount(self):
        self.last_price = (self.price - ((100 - self.discount)/100))
        return self.last_price

class OrderItem(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    order = models.ForeignKey(Order,on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    date_added = models.DateTimeField(default=timezone.now())
