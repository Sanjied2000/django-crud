from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Shop(models.Model):
    ShopName = models.CharField(max_length=255)
    Address = models.TextField()
    Phone = models.CharField(max_length=15)

    def __str__(self):
        return self.ShopName
    

class Fruit(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)  # ForeignKey to Shop
    fruit_name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.fruit_name} - {self.shop.ShopName}"
    
class AdminShop(models.Model):
    user = models.ForeignKey(User ,on_delete=models.CASCADE)
    shop = models.ForeignKey(Shop,on_delete=models.CASCADE)
    

    def __str__(self):
        return f"{self.user.username} - {self.shop.ShopName}"

    
