import json

from django.http import JsonResponse
from django.shortcuts import render
from .models import Customer, Product, Order, OrderedItem
# Create your views here.


def home(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'baajaar_app/home.html', context)


def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(
            customer=customer, completed=False)
        items = order.ordereditem_set.all()
    else:
        items = []
    context = {'items': items, 'order': order}
    return render(request, 'baajaar_app/cart.html', context)


def checkout(request):
    context = {}
    return render(request, 'baajaar_app/checkout.html', context)


def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    print(action)
    print(productId)
    return JsonResponse("added the item", safe=False)
