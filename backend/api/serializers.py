from rest_framework import serializers

from bucket.models import Bucket
from products.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        exclude = ()


class BucketSerializer(serializers.ModelSerializer):
    product_name = serializers.ReadOnlyField()
    product_price = serializers.ReadOnlyField()

    class Meta:
        model = Bucket
        exclude = ()
        read_only_fields = ('user', 'product_name', 'product_price')

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
        attrs.update({'user': self.request_user})
        if self.instance and not count:
            attrs['count'] = self.instance.count + 1
        elif self.instance and count:
            attrs['count'] = count
        else:
            attrs['count'] = 1
        if attrs['count'] > 5:
            raise serializers.ValidationError('Product count should be maximum 5 qty')
        if product.price == 0:
            raise serializers.ValidationError('Product price must be more than zero')
        return attrs


class BucketDestroySerializer(serializers.ModelSerializer):
    class Meta:
        model = Bucket
        exclude = ()
