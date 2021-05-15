from auth_.models import Deliverer
from utils.constants import *
from django.utils import timezone


class OrderManager(models.Manager):
    def get_customer_order(self, customer_id):
        return self.get(customer_id=customer_id)


class Order(models.Model):
    customer = models.ForeignKey("auth_.Customer", on_delete=models.CASCADE, null=True)
    products = models.ManyToManyField("core.Product")
    ordered_at = models.DateField(auto_now_add=True)
    executed = models.BooleanField(default=False)

    objects = OrderManager()

    class Meta:
        verbose_name_plural = 'Orders'
        verbose_name = 'Order'


class DelivererAndOrderManager(models.Manager):
    def get_by_order(self, order_id):
        return self.get(order_id=order_id)


class DelivererAndOrder(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    deliverer = models.ForeignKey(Deliverer, on_delete=models.CASCADE, null=True, blank=True)

    objects = DelivererAndOrderManager()

    class Meta:
        verbose_name_plural = 'Orders and Deliverers'
        verbose_name = 'Order and Deliverer'
