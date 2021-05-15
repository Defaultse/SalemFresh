from django.dispatch import receiver
from django.db.models.signals import post_save
from auth_.models import Profile, CustomUser, Customer


@receiver(post_save, sender=Customer)
def user_created(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=CustomUser)
def update_profile(sender, instance, created, **kwargs):
    if not created:
        instance.profile.save()
        print('Profile created')