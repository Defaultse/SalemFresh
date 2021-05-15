from django.contrib import admin
from auth_.models import *


class Filter(admin.ModelAdmin):
    list_display = ("id", "email", "role", "is_superuser")
    list_filter = ("role",)


admin.site.register(CustomUser, Filter)
admin.site.register(Customer)
admin.site.register(Deliverer)
admin.site.register(Profile)
