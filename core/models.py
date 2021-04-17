from datetime import datetime
from django.db import models
from auth_.models import User
from utils.constants import *


class Shop(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True, db_index=True)
    location = models.CharField(max_length=100, choices=CITIES, blank=True)
    description = models.TextField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name


class ShopOwner(User):
    shop = models.OneToOneField(Shop, unique=True, on_delete=models.PROTECT)

    class Meta:
        verbose_name_plural = 'Владельцы магазинов'
        verbose_name = 'Владелец магазина'


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    location = models.CharField(choices=CITIES, max_length=30 ,blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Клиенты'
        verbose_name = 'Клиент'


class DeliveryGuy(User):
    shopId = models.ForeignKey(Shop, null=True, on_delete=models.PROTECT)

    class Meta:
        verbose_name_plural = 'Доставщик'
        verbose_name = 'Доставщики'


class Category(models.Model):
    name = models.CharField(max_length=180)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, null=True)


class Product(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, null=True)
    price = models.FloatField(max_length=50, null=True, blank=True)
    description = models.TextField(max_length=255, null=True, blank=True)
    # available


class Subscription(models.Model):
    subscriber = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)
    subscribedProduct = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    startedAt = models.DateField(default=datetime.now())
    subscription_interval = models.SmallIntegerField(choices=SUBSCRIPTION_INTERVAL, default=7)


class ShopFeedbacks(models.Model):
    user_id = models.ForeignKey(Customer, null=True, on_delete=models.CASCADE)
    shop_id = models.ForeignKey(Shop, null=True, on_delete=models.CASCADE)
    text = models.TextField(max_length=255, null=True, blank=True)


class ProductFeedbacks(models.Model):
    user_id = models.ForeignKey(Customer, null=True, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, null=True, on_delete=models.CASCADE)
    text = models.TextField(max_length=255, null=True, blank=True)

