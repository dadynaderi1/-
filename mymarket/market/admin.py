from django.contrib import admin
from .models import Category, Product, Order, OrderItem, Cart, CartItem, Review

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Review)
