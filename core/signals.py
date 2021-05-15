from django.dispatch import receiver
from django.db.models.signals import post_save
from core.models.orders import Order, DelivererAndOrder


@receiver(post_save, sender=Order)
def user_created(sender, instance, created, **kwargs):
    if created:
        DelivererAndOrder.objects.create(order=instance)


@receiver(post_save, sender=Order)
def update_order(sender, instance, created, **kwargs):
    if not created:
        instance.order.save()
        print('Profile created')