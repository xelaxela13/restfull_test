from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Bucket(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    products = models.JSONField(blank=True, null=True)
    amount = models.PositiveSmallIntegerField(blank=True, null=True)
