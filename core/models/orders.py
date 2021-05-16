from auth_.models import Deliverer
from utils.constants import *
from django.utils import timezone


class OrderManager(models.Manager):
    def get_customer_orders(self, customer_id):
        return self.filter(customer_id=customer_id)


class Order(models.Model):
    customer = models.ForeignKey("auth_.Customer", on_delete=models.CASCADE, null=True)
    products = models.ManyToManyField("core.Product")
    ordered_at = models.DateField(auto_now_add=True)
    executed = models.BooleanField(default=False)

    objects = OrderManager()

    class Meta:
        verbose_name_plural = 'Orders'
        verbose_name = 'Order'

    def __str__(self):
        if self.executed:
            return 'ORDER ID: {} - executed'.format(self.id)
        else:
            return 'ORDER ID: {} - not executed. Ordered at {}'.format(self.id, self.ordered_at)


class DelivererAndOrderManager(models.Manager):
    def get_by_order(self, order_id):
        return self.get(order_id=order_id)

    def get_by_deliverer(self, deliverer_id):
        deliverers = DelivererAndOrder.objects.filter(deliverer_id=deliverer_id).values_list('order', flat=True)
        orders = Order.objects.filter(id__in=deliverers)
        return orders


class DelivererAndOrder(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    deliverer = models.ForeignKey(Deliverer, on_delete=models.CASCADE, null=True, blank=True)

    objects = DelivererAndOrderManager()

    class Meta:
        verbose_name_plural = 'Orders and Deliverers'
        verbose_name = 'Order and Deliverer'

    def __str__(self):
        return '{}. Deliverer: {}'.format(str(self.order), str(self.deliverer))
