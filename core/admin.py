from django.contrib import admin
from core.models.feedbacks import *
from core.models.profiles import *
from core.models.shop import *

admin.site.register(Customer)
admin.site.register(ShopOwner)
admin.site.register(DeliveryGuy)


admin.site.register(Shop)
admin.site.register(Category)
admin.site.register(Product)

admin.site.register(Subscription)

admin.site.register(ShopFeedbacks)
admin.site.register(ProductFeedbacks)