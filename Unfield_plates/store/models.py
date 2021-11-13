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
    brand = models.CharField(max_length=300,null=True)
    price = models.IntegerField(null=True)
    main_category = models.CharField(max_length=200,null=True)
    main_text = models.TextField(null=True)
    category_1 = models.CharField(max_length=200,null=True)
    category_1_answer = models.CharField(max_length=200,null=True)
    category_2 = models.CharField(max_length=200,null=True)
    category_2_answer = models.CharField(max_length=200,null=True)
    category_3 = models.CharField(max_length=200,null=True)
    category_3_answer = models.CharField(max_length=200,null=True)
    category_4 = models.CharField(max_length=200,null=True)
    category_4_answer = models.CharField(max_length=200,null=True)
    category_5 = models.CharField(max_length=200,null=True)
    category_5_answer = models.CharField(max_length=200,null=True)
    color = models.CharField(max_length=300,null=True)
    main_image = models.ImageField(null=True)
    image2 = models.ImageField(null=True)
    image3 = models.ImageField(null=True)
    image4 = models.ImageField(null=True)
    image5 = models.ImageField(null=True)
    code = models.CharField(max_length=6,unique=True,null=True)

class OrderItem(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    order = models.ForeignKey(Order,on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    date_added = models.DateTimeField(default=timezone.now())
