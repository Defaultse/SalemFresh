from auth_.models import User
from utils.constants import *


class ShopOwner(User):
    shop = models.OneToOneField("core.Shop", unique=True, on_delete=models.PROTECT)

    class Meta:
        verbose_name_plural = 'Владельцы магазинов'
        verbose_name = 'Владелец магазина'


class Customer(User):
    location = models.CharField(choices=CITIES, max_length=30, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Клиенты'
        verbose_name = 'Клиент'


class DeliveryGuy(User):
    shopId = models.ForeignKey("core.Shop", null=True, on_delete=models.PROTECT)

    class Meta:
        verbose_name_plural = 'Доставщик'
        verbose_name = 'Доставщики'
