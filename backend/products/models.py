from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=6)
    category = models.ManyToManyField(Category)

    def __str__(self):
        return f'{self.name} - {self.price}'

    @property
    def category_name_list(self):
        return self.category.values_list('name', flat=True)
