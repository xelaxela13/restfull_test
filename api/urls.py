from django.urls import path
from .views import ProductsList, ProductDetail, BucketList, BucketUpdate

urlpatterns = [
    path('products/', ProductsList.as_view(), name='products'),
    path('products/<int:pk>', ProductDetail.as_view(), name='product'),
    path('buckets', BucketList.as_view(), name='buckets'),
    path('bucket/<int:pk>', BucketUpdate.as_view(), name='bucket'),
]