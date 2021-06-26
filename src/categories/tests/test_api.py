from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from categories.models import CategoryModel
from categories.models import ProviderCategoryModel
from categories.serializers import ProviderCategorySerializer
from categories.serializers import CategorySerializer
from categories.serializers import CategoriesSerializer
from providers.models import ProviderModel


class CategoriesApiTestCase(APITestCase):
    data = None
    detail_data = None

    def setUp(self) -> None:
        data = {'username': 'test_user',
                'email': 'test@localhost.app',
                'password1': 'strongPassword',
                'password2': 'strongPassword',
                }
        self.client.post('/api/rest-auth/registration/', data)

        categories_1 = CategoryModel.objects.create(name='Category_1')
        categories_2 = CategoryModel.objects.create(name='Category_2')
        categories_3 = CategoryModel.objects.create(name='Category_3')
        categories_4 = CategoryModel.objects.create(name='Category_4')
        provider_1 = ProviderModel.objects.create(name='Provider_1')
        ProviderCategoryModel.objects.create(category=categories_1,
                                             provider=provider_1,
                                             url='http://127.0.0.1:8080/api')

        self.data = CategoriesSerializer([categories_1, categories_2, categories_3, categories_4], many=True).data
        self.detail_data = CategorySerializer(categories_1).data

    def test_get_list(self) -> None:
        response = self.client.get(reverse('categories-list'))
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(self.data, response.data.get('results'))

    def test_get_detail(self):
        response = self.client.get(reverse('categories-detail', args=(1,)))
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(self.detail_data, response.data)

    def test_post(self):
        response = self.client.post(reverse('categories-list'), {'name': 'tmpName'})
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        self.assertEqual('tmpName', response.data.get('name'))

    def test_put(self):
        response = self.client.put(reverse('categories-detail', args=(2,)), {'name': 'New Name'})
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual('New Name', response.data.get('name'))

    def test_patch(self):
        response = self.client.put(reverse('categories-detail', args=(2,)), {'name': 'Some Name'})
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual('Some Name', response.data.get('name'))

    def test_delete(self):
        response = self.client.delete(reverse('categories-detail', args=(2,)))
        self.assertEqual(status.HTTP_204_NO_CONTENT, response.status_code)


class ProviderCategoriesApiTestCase(APITestCase):
    detail_data = None

    def setUp(self) -> None:
        data = {'username': 'test_user',
                'email': 'test@localhost.app',
                'password1': 'strongPassword',
                'password2': 'strongPassword',
                }
        self.client.post('/api/rest-auth/registration/', data)

        provider = ProviderModel.objects.create(name='Provider')
        category = CategoryModel.objects.create(name='Category')
        provider_categories_1 = ProviderCategoryModel.objects.create(url='http://127.0.0.1:8080/api/categories/1/',
                                                                     category=category,
                                                                     provider=provider, )

        self.detail_data = ProviderCategorySerializer(provider_categories_1).data

    def test_get_detail(self):
        response = self.client.get(reverse('categories-providers-detail', args=(1, 1)))
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(self.detail_data, response.data)

    def test_post(self):
        response = self.client.post(reverse('categories-providers-post', args=(1,)),
                                    {
                                        "url": "http://127.0.0.1:8080/api/schema/swagger-ui/categories/categories",
                                        "provider": 1,
                                        "category": 1
                                    })
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        self.assertEqual('http://127.0.0.1:8080/api/schema/swagger-ui/categories/categories',
                         response.data.get('url'))

    def test_put(self):
        response = self.client.put(reverse('categories-providers-detail', args=(1, 1,)),
                                   {
                                       "url": "http://127.0.0.1:8080/api/schema",
                                       "provider": 1,
                                       "category": 1
                                   })
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual('http://127.0.0.1:8080/api/schema',
                         response.data.get('url'))

    def test_patch(self):
        response = self.client.patch(reverse('categories-providers-detail', args=(1, 1,)),
                                     {
                                         "url": "http://127.0.0.1:8080/api",
                                         "provider": 1,
                                         "category": 1
                                     })
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual('http://127.0.0.1:8080/api',
                         response.data.get('url'))

    def test_delete(self):
        response = self.client.delete(reverse('categories-providers-detail', args=(1, 1,)))
        self.assertEqual(status.HTTP_204_NO_CONTENT, response.status_code)
