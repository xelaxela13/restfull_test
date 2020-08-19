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
        if self.initial_data.get('id'):
            try:
                self.instance = Bucket.objects.get(id=self.initial_data.get('id'))
            except Bucket.DoesNotExist:
                pass
        if not self.instance:
            attrs.update({'user': self.request_user})
        product = attrs.get('product')
        count = attrs.get('count')
        if not count or count == 0:
            attrs['count'] = count = 1
        if count and count > 5:
            raise serializers.ValidationError('Product count should be maximum 5 pcs')
        if self.instance or product:
            total = Bucket.objects.filter(user_id=self.request_user.id,
                                          product_id=self.instance.product.id
                                          if self.instance else product.id).aggregate(
                total=Sum('count')).get('total')
            if (self.instance and total and total + count - self.instance.count > 5) or (
                    self.instance is None and total and total + count > 5):
                raise serializers.ValidationError('You already has maximum products in bucket')
        return attrs


class BucketUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bucket
        exclude = ()
        read_only_fields = ('user', 'product')

    def __init__(self, *args, **kwargs):
        self.request_user = kwargs.pop('request_user')
        super().__init__(*args, **kwargs)

    def validate(self, attrs):
        count = attrs.get('count')
        if not count or count == 0:
            attrs['count'] = count = 1
        if count and count > 5:
            raise serializers.ValidationError('Product count should be maximum 5 pcs')
        if self.instance:
            total = Bucket.objects.filter(user_id=self.request_user.id, product_id=self.instance.product.id).aggregate(
                total=Sum('count')).get('total')
            if total and total + count > 5:
                raise serializers.ValidationError('You already has maximum products in bucket')
        return attrs
