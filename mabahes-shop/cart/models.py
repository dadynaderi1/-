# cart/models.py
from django.db import models
from users.models import CustomUser  # مدل کاربر
from products.models import Product  # مدل محصول

class Cart(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)  # ارجاع به کاربر
    created_at = models.DateTimeField(auto_now_add=True)  # تاریخ ساخت سبد خرید

    def __str__(self):
        return f"سبد خرید {self.user.username}"

