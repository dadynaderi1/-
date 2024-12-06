from django.db import models
from cart.models import Cart # مدل سبد خرید
from products.models import Product  # مدل محصول
# cart/models.py
class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)  # ارجاع به سبد خرید
    product = models.ForeignKey(Product, on_delete=models.CASCADE)  # ارجاع به محصول
    quantity = models.PositiveIntegerField(default=1)  # تعداد محصول

    def total_price(self):
        # محاسبه قیمت کل برای این آیتم (قیمت محصول × تعداد)
        return self.product.final_price() * self.quantity

    def __str__(self):
        return f"{self.product.name} - {self.quantity} عدد"
