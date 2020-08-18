from rest_framework import generics
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated

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
