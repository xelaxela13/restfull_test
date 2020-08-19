from decimal import Decimal

from django.urls import reverse
from rest_framework.test import APIClient
from products.models import Product


def test_products(user):
    client = APIClient()
    response = client.get(reverse('products'))
    assert response.status_code == 403
    client.login(email=user.email, password='1234567890')
    response = client.get(reverse('products'))
    assert response.status_code == 200
    assert len(response.json()) == Product.objects.exclude(price=0).count()
    first_product = Product.objects.exclude(price=0).first()
    response = client.get(reverse('product', args=(first_product.id,)))
    assert response.status_code == 200
    assert response.json()['name'] == first_product.name


def test_bucket(user):
    client = APIClient()
    response = client.get(reverse('bucket'))
    assert response.status_code == 403
    client.login(email=user.email, password='1234567890')
    response = client.get(reverse('bucket'))
    assert response.status_code == 200
    assert response.json() == {'amount': {'total': None}, 'products': []}

    first_product = Product.objects.exclude(price=0).first()
    last_product = Product.objects.exclude(price=0).last()
    zero_product = Product.objects.filter(price=0).first()

    response = client.post(reverse('bucket'), {'count': 3, 'product': first_product.id})
    assert response.status_code == 201

    response = client.post(reverse('bucket'), {'count': 5, 'product': last_product.id})
    assert response.status_code == 201

    response = client.post(reverse('bucket'), {'count': 3, 'product': zero_product.id})
    assert response.status_code == 400
    assert response.json()['non_field_errors'] == ['Product price must be more than zero']

    response = client.post(reverse('bucket'), {'count': 7, 'product': last_product.id})
    assert response.status_code == 400
    assert response.json()['non_field_errors'] == ['Product count should be maximum 5 qty']

    response = client.get(reverse('bucket'))
    assert response.status_code == 200
    assert len(response.json()['products']) == 2
    assert Decimal(response.json()['amount']['total']).quantize(Decimal('1.00')) == sum(
        Product.objects.get(id=p['product']).price * p['count'] for p in response.json()['products'])
