from django.db import models
from django.contrib.auth.models import AbstractUser
from utils.constants import *


# class Role(models.Model):
#     id = models.PositiveSmallIntegerField(choices=USER_ROLES, primary_key=True)
#
#     def __str__(self):
#         return self.get_id_display()


class User(AbstractUser):
    roles = models.SmallIntegerField(choices=USER_ROLES, default=USER)
    # roles = models.ManyToManyField(Role)
    bio = models.TextField(max_length=500, blank=True)



