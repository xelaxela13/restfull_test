from django.urls import path
from .views import ProductsList, ProductDetail, BucketCreate

urlpatterns = [
    path('products/', ProductsList.as_view(), name='products'),
    path('products/<int:pk>', ProductDetail.as_view(), name='product'),
    path('bucket', BucketCreate.as_view(), name='bucket'),
]