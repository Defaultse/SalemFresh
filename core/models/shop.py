from datetime import datetime
from core.models import Customer
from utils.constants import *


class ShopManager(models.Manager):
    def search(self, name):
        return self.filter(name__contains=name)


class Shop(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True, db_index=True)
    location = models.CharField(max_length=100, choices=CITIES, blank=True)
    description = models.TextField(max_length=255, null=True, blank=True)

    objects = ShopManager()

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=180)
    shop = models.ForeignKey("core.Shop", on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name


class ProductManager(models.Manager):
    def search(self, name):
        return self.filter(name__contains=name)

    def get_by_category(self, category_id):
        return self.get_related().filter(category_id=category_id)


class Product(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, related_name='products')
    shop = models.ForeignKey("core.Shop", on_delete=models.CASCADE, null=True, related_name='products')
    price = models.FloatField(max_length=50, null=True, blank=True)
    description = models.TextField(max_length=255, null=True, blank=True)

    objects = ProductManager()

    def __str__(self):
        return self.name


class Subscription(models.Model):
    subscriber = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)
    subscribedProduct = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    startedAt = models.DateField(default=datetime.now())
    subscription_interval = models.SmallIntegerField(choices=SUBSCRIPTION_INTERVAL, default=7)


