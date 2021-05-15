from utils.constants import *


class Category(models.Model):
    name = models.CharField(max_length=180)

    class Meta:
        verbose_name_plural = 'Categories'
        verbose_name = 'Category'

    def __str__(self):
        return self.name


class ProductManager(models.Manager):
    def search(self, name):
        return self.filter(name__contains=name)

    def get_by_category(self, category_id):
        return self.get_related().filter(category_id=category_id)


class Product(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, related_name='products')
    price = models.FloatField(max_length=50, null=True, blank=True)
    description = models.TextField(max_length=255, null=True, blank=True)
    active = models.BooleanField(null=True, blank=True)

    objects = ProductManager()

    class Meta:
        verbose_name_plural = 'Products'
        verbose_name = 'Product'

    def __str__(self):
        return self.name
