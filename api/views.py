from rest_framework import generics, status
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from api.serializers import ProductSerializer, BucketListSerializer, BucketUpdateSerializer
from bucket.models import Bucket
from products.models import Product


class ProductsList(generics.ListAPIView):
    queryset = Product.objects.exclude(price__lte=0)
    serializer_class = ProductSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (SessionAuthentication,)


class ProductDetail(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (SessionAuthentication,)


class BucketList(generics.ListAPIView):
    queryset = Bucket.objects.all()
    serializer_class = BucketListSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (SessionAuthentication,)


class BucketUpdate(generics.RetrieveUpdateAPIView):
    queryset = Bucket.objects.all()
    serializer_class = BucketUpdateSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (SessionAuthentication,)

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user_id=self.request.user.id)

    def get_serializer(self, *args, **kwargs):
        serializer_class = self.get_serializer_class()
        kwargs['request_user'] = self.request.user
        return serializer_class(*args, **kwargs)
