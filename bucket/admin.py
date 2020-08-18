from django.contrib import admin

from bucket.models import Bucket


@admin.register(Bucket)
class Bucket(admin.ModelAdmin):
    pass
