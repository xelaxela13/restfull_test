from rest_framework import generics, status
from rest_framework.authentication import SessionAuthentication
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from api.serializers import ProductSerializer, BucketSerializer
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


class BucketCreate(generics.ListCreateAPIView):
    queryset = Bucket.objects.all()
    serializer_class = BucketSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (SessionAuthentication,)

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user_id=self.request.user.id)

    def get_serializer(self, *args, **kwargs):
        serializer_class = self.get_serializer_class()
        kwargs['request_user'] = self.request.user
        return serializer_class(*args, **kwargs)
