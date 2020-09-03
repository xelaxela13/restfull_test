from django.db import models
from accounts.models import User
from products.models import Product


class BucketItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    count = models.PositiveSmallIntegerField(default=1)

    @property
    def product_name(self):
        return self.product.name

    @property
    def product_price(self):
        return self.product.price

    @property
    def product_category(self):
        return self.product.category.values('pk', 'name')
