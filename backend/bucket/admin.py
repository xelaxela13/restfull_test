from django.contrib import admin

from bucket.models import BucketItem


@admin.register(BucketItem)
class Bucket(admin.ModelAdmin):
    pass
