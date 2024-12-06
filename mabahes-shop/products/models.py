# products/models.py
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)  # نام محصول
    description = models.TextField(blank=True, null=True)  # توضیحات
    price = models.DecimalField(max_digits=10, decimal_places=2)  # قیمت
    image = models.ImageField(upload_to='products/')  # تصویر
    discount = models.PositiveIntegerField(default=0)  # تخفیف درصدی

    def final_price(self):
        # محاسبه قیمت نهایی با توجه به تخفیف
        return self.price - (self.price * self.discount / 100)

    def __str__(self):
        return self.name
