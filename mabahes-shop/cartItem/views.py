# cart/views.py
from django.shortcuts import redirect
from .models import CartItem

def remove_item(request, item_id):
    item = CartItem.objects.get(id=item_id)
    item.delete()
    return redirect('cart_view')
