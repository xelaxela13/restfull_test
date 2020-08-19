from django.urls import path
from .views import ProductsList, ProductDetail, BucketAPIView, BucketDestroy, BucketClear

urlpatterns = [
    path('products/', ProductsList.as_view(), name='products'),
    path('products/<int:pk>', ProductDetail.as_view(), name='product'),
    path('bucket/', BucketAPIView.as_view(), name='bucket'),
    path('bucket/<int:pk>', BucketDestroy.as_view(), name='bucket-delete'),
    path('bucket/clear/', BucketClear.as_view(), name='bucket-clear'),
]
