from os.path import exists

from django.db.models import F
from django.dispatch import receiver
from django.db.models.signals import post_save, pre_save
from django.shortcuts import get_object_or_404
from rest_framework.response import Response

from auth_.models import Deliverer
from core.models.orders import Order, DelivererAndOrder


@receiver(post_save, sender=Order)
def order_created(sender, instance, created, **kwargs):
    if created:
        DelivererAndOrder.objects.create(order=instance)


@receiver(post_save, sender=Order)
# If manager assigned delivery guy to the order!
def on_order_confirmation(sender, instance: Order, **kwargs):
    delivererAndOrder = DelivererAndOrder.objects.get(order_id=instance.id)
    if delivererAndOrder.deliverer is not None:
        cnt = get_object_or_404(Deliverer, id=delivererAndOrder.deliverer.id)
        cnt = Deliverer.objects.get(id=delivererAndOrder.deliverer.id)
        cnt.completed_orders_count += 1
        cnt.save()
    else:
        Response("Deliverer is not assigned yet.")

