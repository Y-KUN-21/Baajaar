import uuid

from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Customer(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, null=True, blank=True, name="customer")
    name = models.CharField(max_length=200)
    profilePic = models.ImageField(upload_to='profile/')
    email = models.EmailField(max_length=200)

    def __str__(self):
        return self.name

    @property
    def profilePicURL(self):
        try:
            url = self.profilePic.url
        except:
            url = ''
        return url


class Product(models.Model):
    brand = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='product/', null=True)

    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url


class Order(models.Model):
    customer = models.ForeignKey(
        Customer, on_delete=models.SET_NULL, null=True, blank=True)
    order_date = models.DateField(auto_now_add=True)
    completed = models.BooleanField(default=False, null=True, blank=True)
    transactionId = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)

    def __str__(self):
        return str(self.transactionId)

    @property
    def get_grand_total(self):
        ordered_items = self.ordereditem_set.all()
        grand_total = sum([item.get_total for item in ordered_items])
        return grand_total

    @property
    def get_cart_items(self):
        ordered_items = self.ordereditem_set.all()
        total = sum([item.quantity for item in ordered_items])
        return total

    @property
    def shipping(self):
        shipping = False
        ordered_items = OrderedItem.objects.all().count()
        if ordered_items > 0:
            shipping = True
        return shipping


class OrderedItem(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.SET_NULL, null=True, blank=True)
    order = models.ForeignKey(
        Order, on_delete=models.SET_NULL, null=True, blank=True)
    order_date = models.DateField(auto_now_add=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total


class ShippingAdress(models.Model):
    customer = models.ForeignKey(
        Customer, on_delete=models.SET_NULL, null=True, blank=True)
    order = models.ForeignKey(
        Order, on_delete=models.SET_NULL, null=True, blank=True)
    firstname = models.CharField(null=True, blank=True, max_length=250)
    lastname = models.CharField(null=True, blank=True, max_length=250)
    address = models.CharField(null=True, blank=True, max_length=1000)
    city = models.CharField(null=True, blank=True, max_length=250)
    zipcode = models.CharField(null=True, blank=True, max_length=250) 
    state = models.CharField(null=True, blank=True, max_length=700)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.Address
