from django.urls import path
from .views import ProductsList, ProductDetail, BucketAPIView, BucketDestroy, BucketClear

urlpatterns = [
    path('api/products/', ProductsList.as_view(), name='products'),
    path('api/products/<int:pk>', ProductDetail.as_view(), name='product'),
    path('api/bucket/', BucketAPIView.as_view(), name='bucket'),
    path('api/bucket/<int:pk>', BucketDestroy.as_view(), name='bucket-delete'),
    path('api/bucket/clear/', BucketClear.as_view(), name='bucket-clear'),
]
