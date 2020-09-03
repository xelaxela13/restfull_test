from rest_framework import serializers

from bucket.models import BucketItem
from products.models import Product


class ProductSerializer(serializers.ModelSerializer):
    category_name_list = serializers.ReadOnlyField()

    class Meta:
        model = Product
        exclude = ()
        read_only_fields = ('category_name_list',)


class BucketSerializer(serializers.ModelSerializer):
    product_name = serializers.ReadOnlyField()
    product_price = serializers.ReadOnlyField()
    product_category = serializers.ReadOnlyField()

    class Meta:
        model = BucketItem
        exclude = ()
        read_only_fields = ('user', 'product_name', 'product_price', 'product_category')

    def __init__(self, *args, **kwargs):
        self.request_user = kwargs.pop('request_user')
        super().__init__(*args, **kwargs)

    def validate(self, attrs):
        product = attrs.get('product')
        count = attrs.get('count')
        bucket_id = self.initial_data.get('id')
        # its not required request to DB, I know about this, maybe in real project this is not good solutions
        if bucket_id:
            try:
                self.instance = BucketItem.objects.get(id=bucket_id)
            except BucketItem.DoesNotExist:
                pass
        if self.instance is None:
            try:
                self.instance = BucketItem.objects.get(product_id=product.id)
            except BucketItem.DoesNotExist:
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
        model = BucketItem
        exclude = ()
