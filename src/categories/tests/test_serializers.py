from django.test import TestCase
from categories.models import ProviderCategoryModel
from categories.models import CategoryModel
from categories.serializers import CategorySerializer
from categories.serializers import ProviderCategorySerializer
from categories.serializers import CategoriesSerializer
from providers.models import ProviderModel


class CategoriesSerializerTestCase(TestCase):

    def test_ok(self):
        categories_1 = CategoryModel.objects.create(name='Category_1')
        categories_2 = CategoryModel.objects.create(name='Category_2')
        data = CategoriesSerializer([categories_1, categories_2], many=True).data
        expected_data = [
            {
                'id': categories_1.id,
                'name': 'Category_1',
                'created': categories_1.created.strftime('%Y-%m-%d')
            },
            {
                'id': categories_2.id,
                'name': 'Category_2',
                'created': categories_2.created.strftime('%Y-%m-%d')
            },
        ]

        self.assertEqual(expected_data, data)


class CategorySerializerTestCase(TestCase):

    def test_ok(self):
        categories = CategoryModel.objects.create(name='Category')
        data = CategorySerializer(categories).data
        self.assertEqual(categories.name, data.get('name'))


class ProviderCategorySerializerTestCase(TestCase):

    def test_ok(self):
        provider = ProviderModel.objects.create(name='Provider')
        category = CategoryModel.objects.create(name='Category')
        provider_category = ProviderCategoryModel.objects.create(url='https://www.youtube.com',
                                                                 provider=provider,
                                                                 category=category)
        data = ProviderCategorySerializer(provider_category).data

        expected_data = {
            'url': 'https://www.youtube.com',
            'provider': 1,
            'category': 1
        }

        self.assertEqual(expected_data, data)
