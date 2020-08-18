from rest_framework import serializers

from bucket.models import Bucket
from products.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        exclude = ()


class BucketListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bucket
        exclude = ()


class BucketUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bucket
        fields = ('user', 'amount', 'products')
        read_only_fields = ('user', 'amount')

    def __init__(self, *args, **kwargs):
        self.request_user = kwargs.pop('request_user')
        super().__init__(*args, **kwargs)

    def validate(self, attrs):
        attrs.update({'user': self.request_user})
        # attrs.update({'amount': sum(p.price for p in attrs['products'])})
        product_id = attrs.get('products')
        if product_id and product_id.isdigit():
            try:
                product = Product.objects.get(pk=product_id)
                attrs['products'] = {'products': [product_id]}
            except Product.DoesNotExist:
                raise serializers.ValidationError(f'Product with id {product_id} does not exist')
        elif not product_id or not product_id.isdigit():
            raise serializers.ValidationError('Expected product ID')
        return attrs
