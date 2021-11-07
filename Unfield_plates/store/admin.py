from django.contrib import admin
from .models import Order,ShippingAddress,OrderItem,Product
# Register your models here.

admin.site.register(Order)
admin.site.register(ShippingAddress)
admin.site.register(OrderItem)
admin.site.register(Product)
