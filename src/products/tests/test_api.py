from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from categories.models import CategoryModel
from products.models import ProductModel
from products.models import ProviderProductModel
from products.serializers import ProductsSerializer
from products.serializers import ProviderProductSerializer
from products.serializers import ProviderProductsSerializer
from providers.models import ProviderModel


class ProductApiTestCase(APITestCase):
    data = None
    detail_data = None

    def setUp(self) -> None:
        data = {'username': 'test_user',
                'email': 'test@localhost.app',
                'password1': 'strongPassword',
                'password2': 'strongPassword',
                }
        self.client.post('/api/rest-auth/registration/', data)

        categories1 = CategoryModel.objects.create(name='Category_1')
        categories2 = CategoryModel.objects.create(name='Category_2')
        product_1 = ProductModel.objects.create(category=categories1)
        product_2 = ProductModel.objects.create(category=categories1)

        self.data = ProductsSerializer([product_1, product_2], many=True).data
        self.detail_data = ProductsSerializer(product_1).data

    def test_get_list(self) -> None:
        response = self.client.get(reverse('product-list'))
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(self.data, response.data.get('results'))

    def test_get_detail(self):
        response = self.client.get(reverse('product-detail', args=(1,)))
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(self.detail_data, response.data)

    def test_post(self):
        response = self.client.post(reverse('product-list'), {'category': 1})
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        self.assertEqual(1, response.data.get('category'))

    def test_put(self):
        response = self.client.put(reverse('product-detail', args=(2,)), {'category': 2})
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(2, response.data.get('category'))

    def test_patch(self):
        response = self.client.put(reverse('product-detail', args=(1,)), {'category': 2})
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(2, response.data.get('category'))

    def test_delete(self):
        response = self.client.delete(reverse('product-detail', args=(2,)))
        self.assertEqual(status.HTTP_204_NO_CONTENT, response.status_code)


class ProviderProductApiTestCase(APITestCase):
    detail_data = None
    data = None

    def setUp(self) -> None:
        data = {'username': 'test_user',
                'email': 'test@localhost.app',
                'password1': 'strongPassword',
                'password2': 'strongPassword',
                }
        self.client.post('/api/rest-auth/registration/', data)

        category = CategoryModel.objects.create(name='Category')
        provider = ProviderModel.objects.create(name='Provider')
        product = ProductModel.objects.create(category=category)
        provider_product_1 = ProviderProductModel.objects.create(name='provider_product',
                                                                 price=25.23,
                                                                 code=32543465,
                                                                 provide=provider,
                                                                 product=product)
        provider_product_2 = ProviderProductModel.objects.create(name='provider_product',
                                                                 price=55.48,
                                                                 code=32543345,
                                                                 provide=provider,
                                                                 product=product)

        self.detail_data = ProviderProductSerializer(provider_product_1).data
        self.data = ProviderProductsSerializer([provider_product_1, provider_product_2], many=True).data

    def test_get_list(self):
        response = self.client.get(reverse('providers-product-list', args=(1,)))
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(self.data, response.data.get('results'))

    def test_get_detail(self):
        response = self.client.get(reverse('providers-product-detail', args=(1, 1)))
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(self.detail_data, response.data)

    def test_post(self):
        response = self.client.post(reverse('providers-product-list', args=(1,)),
                                    {
                                        'name': 'new name',
                                        'price': 233.21,
                                        'code': 2143255,
                                        'provide': 1,
                                        'product': 1
                                    })
        expected_data = {
            'id': 3,
            'name': 'new name',
            'price': 233.21,
            'code': 2143255,
            'created': response.data.get('created'),
            'product': 1,
            'provide': 1
        }
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        self.assertEqual(expected_data, response.data)

    def test_put(self):
        response = self.client.put(reverse('providers-product-detail', args=(1, 1)),
                                   {
                                       'name': 'changed name',
                                       'price': 324.32,
                                       'code': 3125235,
                                       'provide': 1,
                                       'product': 1
                                   })
        expected_data = {
            'id': 1,
            'name': 'changed name',
            'price': 324.32,
            'code': 3125235,
            'created': response.data.get('created'),
            'product': 1,
            'provide': 1
        }

        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(expected_data, response.data)

    def test_patch(self):
        response = self.client.patch(reverse('providers-product-detail', args=(1, 2)),
                                     {
                                         'name': 'patch name',
                                         'price': 34324.234,
                                         'code': 414513325,
                                         'provide': 1,
                                         'product': 1
                                     })
        expected_data = {
            'id': 2,
            'name': 'patch name',
            'price': 34324.234,
            'code': 414513325,
            'created': response.data.get('created'),
            'product': 1,
            'provide': 1
        }

        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(expected_data, response.data)

    def test_delete(self):
        response = self.client.delete(reverse('providers-product-detail', args=(1, 1,)))
        self.assertEqual(status.HTTP_204_NO_CONTENT, response.status_code)
