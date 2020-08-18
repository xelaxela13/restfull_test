from django.contrib.auth import get_user_model
from django.db import models

from products.models import Product

User = get_user_model()


class Bucket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    amount = models.PositiveSmallIntegerField()
