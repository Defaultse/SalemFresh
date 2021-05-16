from utils.constants import *


class ShopFeedback(models.Model):
    user_id = models.ForeignKey("auth_.Customer", null=True, on_delete=models.CASCADE)
    text = models.TextField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.text


class ProductFeedbackManager(models.Manager):
    def get_feedbacks(self, id):
        return self.filter(product_id=id)


class ProductFeedback(models.Model):
    user_id = models.ForeignKey("auth_.Customer", null=True, on_delete=models.CASCADE)
    product_id = models.ForeignKey("core.Product", null=True, on_delete=models.CASCADE)
    text = models.TextField(max_length=255, null=True, blank=True)

    objects = ProductFeedbackManager()

    def __str__(self):
        return '{}, {}'.format(self.product_id, self.text)