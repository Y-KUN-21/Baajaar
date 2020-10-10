from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('checkout/', views.checkout, name='checkout'),
    path('cart/', views.cart, name='cart'),
    path('update-item/', views.updateItem, name='update'),
    path('process-order/', views.processOrder, name='process_order')

]
