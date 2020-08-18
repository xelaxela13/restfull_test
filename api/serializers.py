from rest_framework import serializers

from bucket.models import Bucket
from products.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        exclude = ()


class BucketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bucket
        exclude = ()
