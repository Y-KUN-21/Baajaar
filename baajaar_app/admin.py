from django.contrib import admin
from .models import Customer, Product, OrderedItem, Order, ShippingAdress
# Register your models here.

admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderedItem)
admin.site.register(ShippingAdress)
