import json

from django.http import JsonResponse
from django.shortcuts import render
from .models import Customer, Product, Order, OrderedItem, ShippingAdress


# Create your views here.


def home(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(
            customer=customer, completed=False)
        items = order.ordereditem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}
        cartItems = order['get_cart_items']
    products = Product.objects.all()
    context = {'products': products, 'cartItems': cartItems}
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
    customer = request.user.customer
    order, created = Order.objects.get_or_create(
        customer=customer, completed=False)
    context = {'order': order}
    return render(request, 'baajaar_app/checkout.html', context)


def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    print("PRODUCT ID ==" + productId)
    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(
        customer=customer, completed=False)

    Ordered_Item, created = OrderedItem.objects.get_or_create(
        order=order, product=product)

    if action == "add":
        Ordered_Item.quantity = (Ordered_Item.quantity + 1)
    elif action == 'remove':
        Ordered_Item.quantity = (Ordered_Item.quantity - 1)

    Ordered_Item.save()

    if Ordered_Item.quantity <= 0:
        Ordered_Item.delete()

    return JsonResponse("added the item", safe=False)


def processOrder(request):
    data = json.loads(request.body)
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(
            customer=customer, completed=False)
        total = float(data['form']['total'])

        if total == Order.get_cart_total:
            order.completed = True
        order.save()

        if order.shipping:
            ShippingAdress.objects.create(
                customer=customer,
                order=order,
                firstname=data['shipping']['firstName'],
                lastname=data['shipping']['lastName'],
                address=data['shipping']['Address'],
                state=data['shipping']['state'],
                zipcode=data['shipping']['zip'],

            )
    else:
        print("bruh...................user is not authenticated")
    return JsonResponse('Payment completed', safe=False)
