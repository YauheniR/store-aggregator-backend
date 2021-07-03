from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from categories.models import CategoryModel
from products.models import ProductModel
from products.models import ProviderProductModel
from products.serializers import ProviderProductSerializer
from products.serializers import ProviderProductsSerializer
from providers.models import ProviderModel


class UserRegistration:
    _user_data_ = {
        'username': 'test_user',
        'email': 'test@localhost.app',
        'password1': 'strongPassword',
        'password2': 'strongPassword',
    }

    @staticmethod
    def registration(test_case):
        test_case.client.post('/api/rest-auth/registration/', UserRegistration._user_data_)


class ProductApiTestCase(APITestCase):
    data = None
    detail_data = None

    def setUp(self) -> None:
        UserRegistration.registration(self)

        CategoryModel.objects.bulk_create([CategoryModel(name='Category_1'),
                                           CategoryModel(name='Category_2'), ])

        self.data = ProductModel.objects.bulk_create([ProductModel(category=CategoryModel.objects.get(id=1)),
                                                      ProductModel(category=CategoryModel.objects.get(id=1))])
        self.detail_data = self.data[0]

    def test_get_products_call_200_ok(self) -> None:
        response = self.client.get(reverse('products_list'))
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(CategoryModel.objects.count(), len(self.data))

    def test_get_product_call_200_ok(self):
        response = self.client.get(reverse('product_detail', args=(1,)))
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(response.data.get('category'), self.detail_data.category.id)
        self.assertEqual(response.data.get('created'), self.detail_data.created.strftime('%Y-%m-%d'))

    def test_post_product_call_201_created(self):
        response = self.client.post(reverse('products_list'), {'category': 1})
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        self.assertEqual(1, response.data.get('category'))

    def test_put_product_call_200_ok(self):
        response = self.client.put(reverse('product_detail', args=(2,)), {'category': 2})
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(2, response.data.get('category'))

    def test_patch_product_call_200_ok(self):
        response = self.client.patch(reverse('product_detail', args=(1,)), {'category': 2})
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(2, response.data.get('category'))

    def test_delete_product_call_204_no_content(self):
        response = self.client.delete(reverse('product_detail', args=(2,)))
        self.assertEqual(status.HTTP_204_NO_CONTENT, response.status_code)


class ProviderProductApiTestCase(APITestCase):
    detail_data = None
    data = None

    def setUp(self) -> None:
        UserRegistration.registration(self)

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

    def test_get_provider_products_call_200_ok(self):
        response = self.client.get(reverse('providers_product_list', args=(1,)))
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(self.data, response.data.get('results'))

    def test_get_provider_product_call_200_ok(self):
        response = self.client.get(reverse('providers_product_detail', args=(1, 1)))
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(self.detail_data, response.data)

    def test_post_provider_product_call_201_created(self):
        response = self.client.post(reverse('providers_product_list', args=(1,)), {'name': 'tmpName',
                                                                                   'price': 235.235,
                                                                                   'code': 32526,
                                                                                   'product': 1,
                                                                                   'provide': 1,
                                                                                   })
        new_provider_product = ProviderProductModel.objects.get(id=3)
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        self.assertEqual(response.data.get('name'), new_provider_product.name)
        self.assertEqual(response.data.get('created'), new_provider_product.created.strftime('%Y-%m-%d'))

    def test_put_provider_product_call_200_ok(self):
        response = self.client.put(reverse('providers_product_detail', args=(1, 1)),
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

    def test_patch_provider_product_call_200_ok(self):
        response = self.client.patch(reverse('providers_product_detail', args=(1, 2)),
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

    def test_delete_provider_product_call_201_no_content(self):
        response = self.client.delete(reverse('providers_product_detail', args=(1, 1,)))
        self.assertEqual(status.HTTP_204_NO_CONTENT, response.status_code)
