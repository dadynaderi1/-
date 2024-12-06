from django.shortcuts import render
from .models import Cart, CartItem

def cart_view(request):
    # دریافت سبد خرید کاربر
    cart = Cart.objects.get(user=request.user)
    cart_items = CartItem.objects.filter(cart=cart)
    total_price = sum(item.total_price() for item in cart_items)
    
    context = {
        'cart_items': cart_items,
        'total_price': total_price
    }
    
    return render(request, 'cart/cart.html', context)
