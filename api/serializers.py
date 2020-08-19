from django.db.models import Sum
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
        attrs.update({'user': self.request_user})
        product = attrs.get('product')
        count = attrs.get('count')
        if count and count > 5:
            raise serializers.ValidationError('Product count should be maximum 5 pcs')
        if product:
            total = Bucket.objects.filter(user_id=self.request_user.id, product_id=product.id).aggregate(
                total=Sum('count')).get('total')
            if total and total + count > 5:
                raise serializers.ValidationError('You already has maximum products in bucket')
        return attrs
