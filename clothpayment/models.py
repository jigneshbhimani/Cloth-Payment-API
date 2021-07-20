from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Cloth(models.Model):
    item = models.CharField(max_length=50,blank=False)
    price = models.IntegerField(unique=True)
    description = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.item}"

    class Meta:
        ordering = ['-created_at']



class Cart(models.Model):
    cart = models.OneToOneField(User,on_delete=models.CASCADE)
    clothes = models.ManyToManyField(Cloth)
    created_at = models.DateTimeField(auto_now_add=True)
    quantity = models.PositiveIntegerField(default=1)

    class Meta:
        ordering = ['cart','-created_at']

    def __str__(self):
        return f"{self.cart}"

    @property
    def total(self):
        total = 0
        for item in self.clothes.all():
            total += int(item.quantity) * float(item.clothes.price)
        return total

class Order(models.Model):
    cart = models.ForeignKey(Cart,on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    shipping_charge = models.IntegerField(default=100)

    def __str__(self):
        return f"{self.cart}"

    @property
    def cart_total(self):
        return self.cart.total

    @property
    def final_total(self):
        final_total = float(self.cart_total) + float(self.shipping_charge)
        return final_total