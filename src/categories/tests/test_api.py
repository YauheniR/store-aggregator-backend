from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from categories.models import CategoryModel
from categories.models import ProviderCategoryModel
from categories.serializers import ProviderCategorySerializer
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


class CategoriesApiTestCase(APITestCase):
    data = None
    detail_data = None

    def setUp(self) -> None:
        UserRegistration.registration(self)
        self.data = CategoryModel.objects.bulk_create([CategoryModel(name='Category_1'),
                                                       CategoryModel(name='Category_2'),
                                                       CategoryModel(name='Category_3'),
                                                       CategoryModel(name='Category_4'), ])
        self.detail_data = self.data[0]

    def test_get_categories_call_200_ok(self):
        response = self.client.get(reverse('categories_list'))
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(CategoryModel.objects.count(), len(self.data))

    def test_get_category_call_200_ok(self):
        response = self.client.get(reverse('category_detail', args=(1,)))
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(response.data.get('name'), self.detail_data.name)
        self.assertEqual(response.data.get('created'), self.detail_data.created.strftime('%Y-%m-%d'))

    def test_post_category_call_201_created(self):
        response = self.client.post(reverse('categories_list'), {'name': 'tmpName'})
        new_category = CategoryModel.objects.get(id=5)
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        self.assertEqual(response.data.get('name'), new_category.name)
        self.assertEqual(response.data.get('created'), new_category.created.strftime('%Y-%m-%d'))

    def test_put_category_call_200_ok(self):
        response = self.client.put(reverse('category_detail', args=(2,)), {'name': 'New Name'})
        put_category = CategoryModel.objects.get(id=2)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(response.data.get('name'), put_category.name)
        self.assertEqual(response.data.get('created'), put_category.created.strftime('%Y-%m-%d'))

    def test_patch_category_call_200_ok(self):
        response = self.client.patch(reverse('category_detail', args=(3,)), {'name': 'Some Name'})
        patch_category = CategoryModel.objects.get(id=3)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(response.data.get('name'), patch_category.name)
        self.assertEqual(response.data.get('created'), patch_category.created.strftime('%Y-%m-%d'))

    def test_delete_category_call_204_no_content(self):
        response = self.client.delete(reverse('category_detail', args=(2,)))
        self.assertEqual(status.HTTP_204_NO_CONTENT, response.status_code)


class ProviderCategoriesApiTestCase(APITestCase):
    detail_data = None
    url_provider_category = 'http://127.0.0.1:8080/api/categories/1/'
    url_post = 'http://127.0.0.1:8080/api/schema/swagger-ui/categories/categories'
    url_put = 'http://127.0.0.1:8080/api/schema'
    url_patch = 'http://127.0.0.1:8080/api'

    def setUp(self) -> None:
        UserRegistration.registration(self)

        provider = ProviderModel.objects.create(name='Provider')
        category = CategoryModel.objects.create(name='Category')
        provider_categories_1 = ProviderCategoryModel.objects.create(url=self.url_provider_category,
                                                                     category=category,
                                                                     provider=provider, )

        self.detail_data = ProviderCategorySerializer(provider_categories_1).data

    def test_get_provider_category_call_200_ok(self):
        response = self.client.get(reverse('categories_providers_detail', args=(1, 1)))
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(self.detail_data, response.data)

    def test_post_provider_category_call_201_created(self):
        response = self.client.post(reverse('categories_providers_post', args=(1,)),
                                    {
                                        "url": self.url_post,
                                        "provider": 1,
                                        "category": 1
                                    })
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        self.assertEqual(self.url_post,
                         response.data.get('url'))

    def test_put_provider_category_call_200_ok(self):
        response = self.client.put(reverse('categories_providers_detail', args=(1, 1,)),
                                   {
                                       "url": self.url_put,
                                       "provider": 1,
                                       "category": 1
                                   })
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(self.url_put,
                         response.data.get('url'))

    def test_patch_provider_category_call_200_ok(self):
        response = self.client.patch(reverse('categories_providers_detail', args=(1, 1,)),
                                     {
                                         "url": self.url_patch,
                                         "provider": 1,
                                         "category": 1
                                     })
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(self.url_patch,
                         response.data.get('url'))

    def test_delete_provider_category_call_204_no_content(self):
        response = self.client.delete(reverse('categories_providers_detail', args=(1, 1,)))
        self.assertEqual(status.HTTP_204_NO_CONTENT, response.status_code)
