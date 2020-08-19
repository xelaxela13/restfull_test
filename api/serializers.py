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
        read_only_fields = ('user',)

    def __init__(self, *args, **kwargs):
        self.request_user = kwargs.pop('request_user')
        super().__init__(*args, **kwargs)

    def validate(self, attrs):
        product = attrs.get('product')
        count = attrs.get('count')
        bucket_id = self.initial_data.get('id')
        if bucket_id:
            try:
                self.instance = Bucket.objects.get(id=bucket_id)
            except Bucket.DoesNotExist:
                pass
        if self.instance is None:
            try:
                self.instance = Bucket.objects.get(product_id=product.id)
            except Bucket.DoesNotExist:
                pass
        if not self.instance:
            attrs.update({'user': self.request_user})
        if not count or count == 0:
            attrs['count'] = count = 1
        if count and count > 5:
            raise serializers.ValidationError('Product count should be maximum 5 qty')
        if product.price == 0:
            raise serializers.ValidationError('Product price must be more than zero')
        return attrs


class BucketDestroySerializer(serializers.ModelSerializer):
    class Meta:
        model = Bucket
        exclude = ()
