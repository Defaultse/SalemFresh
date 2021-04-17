from utils.constants import *


class ShopFeedbacks(models.Model):
    user_id = models.ForeignKey("core.Customer", null=True, on_delete=models.CASCADE)
    shop_id = models.ForeignKey("core.Shop", null=True, on_delete=models.CASCADE)
    text = models.TextField(max_length=255, null=True, blank=True)

    class Meta:
        app_label = 'core'


class ProductFeedbacks(models.Model):
    user_id = models.ForeignKey("core.Customer", null=True, on_delete=models.CASCADE)
    product_id = models.ForeignKey("core.Product", null=True, on_delete=models.CASCADE)
    text = models.TextField(max_length=255, null=True, blank=True)