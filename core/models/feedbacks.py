from utils.constants import *


class ShopFeedback(models.Model):
    user_id = models.ForeignKey("auth_.Customer", null=True, on_delete=models.CASCADE)
    text = models.TextField(max_length=255, null=True, blank=True)


class ProductFeedback(models.Model):
    user_id = models.ForeignKey("auth_.Customer", null=True, on_delete=models.CASCADE)
    product_id = models.ForeignKey("core.Product", null=True, on_delete=models.CASCADE)
    text = models.TextField(max_length=255, null=True, blank=True)