from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.PositiveSmallIntegerField()
    category = models.ManyToManyField(Category)

    def __str__(self):
        return f'{self.name} - {self.price}'
