from django.contrib import admin

from products.models import Product, Category


@admin.register(Product)
class ProductsAdmin(admin.ModelAdmin):
    filter_horizontal = ('category',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass
