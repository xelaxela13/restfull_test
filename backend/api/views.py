from django.db.models import Sum, F, DecimalField
from rest_framework import generics, status
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter

from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from api.serializers import ProductSerializer, BucketSerializer, BucketDestroySerializer
from bucket.models import Bucket
from products.models import Product


class ProductsList(generics.ListAPIView):
    queryset = Product.objects.exclude(price__lte=0)
    serializer_class = ProductSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    filterset_fields = ['price', 'category__name']
    ordering_fields = ['price', ]
    search_fields = ['name', 'description']


class ProductDetail(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsAuthenticated,)


class BucketAPIView(generics.ListCreateAPIView):
    queryset = Bucket.objects.all()
    serializer_class = BucketSerializer
    permission_classes = (IsAuthenticated,)

    def get_serializer(self, *args, **kwargs):
        serializer_class = self.get_serializer_class()
        kwargs['request_user'] = self.request.user
        return serializer_class(*args, **kwargs)

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user_id=self.request.user.id)

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        data = {
            'products': serializer.data,
            'amount': serializer.instance.aggregate(total=Sum(F('product__price') * F('count'),
                                                              output_field=DecimalField(decimal_places=2)))
        }
        return Response(data)


class BucketDestroy(generics.DestroyAPIView):
    queryset = Bucket.objects.all()
    serializer_class = BucketDestroySerializer
    permission_classes = (IsAuthenticated,)


class BucketClear(APIView):
    permission_classes = (IsAuthenticated,)

    def delete(self, request, *args, **kwargs):
        Bucket.objects.filter(user_id=request.user.id).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
