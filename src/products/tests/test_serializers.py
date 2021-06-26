from django.test import TestCase
from categories.models import CategoryModel
from products.models import ProductModel
from products.models import ProviderProductModel
from products.serializers import ProductsSerializer
from products.serializers import ProviderProductsSerializer
from providers.models import ProviderModel


class ProductsSerializerTestCase(TestCase):

    def test_ok(self):
        category = CategoryModel.objects.create(name='Category')
        product = ProductModel.objects.create(category=category)
        data = ProductsSerializer(product).data
        expected_data = {
            'id': 1,
            'created': data.get('created'),
            'category': 1
        }
        self.assertEqual(expected_data, data)


class ProviderProductsSerializerTestCase(TestCase):
    def test_ok(self):
        category = CategoryModel.objects.create(name='Category')
        product = ProductModel.objects.create(category=category)
        provider = ProviderModel.objects.create(name='Provider')
        provider_product_1 = ProviderProductModel.objects.create(name='provider_product_1',
                                                                 code=353464567,
                                                                 price=124.123,
                                                                 provide=provider,
                                                                 product=product)
        provider_product_2 = ProviderProductModel.objects.create(name='provider_product_2',
                                                                 code=2141,
                                                                 price=1435.31,
                                                                 provide=provider,
                                                                 product=product)
        data = ProviderProductsSerializer([provider_product_1, provider_product_2], many=True).data

        expected_data = [
            {
                'id': 1,
                'name': 'provider_product_1',
                'price': 124.123,
                'code': 353464567,
                'created': provider_product_1.created.strftime('%Y-%m-%d'),
                'product': 1,
                'provide': 1
            },
            {
                'id': 2,
                'name': 'provider_product_2',
                'price': 1435.31,
                'code': 2141,
                'created': provider_product_2.created.strftime('%Y-%m-%d'),
                'product': 1,
                'provide': 1
            },
        ]

        self.assertEqual(expected_data, data)


class ProviderProductSerializerTestCase(TestCase):
    def test_ok(self):
        category = CategoryModel.objects.create(name='Category')
        product = ProductModel.objects.create(category=category)
        provider = ProviderModel.objects.create(name='Provider')
        provider_product = ProviderProductModel.objects.create(name='provider_product',
                                                               code=574574,
                                                               price=143321.13,
                                                               provide=provider,
                                                               product=product)

        data = ProviderProductsSerializer(provider_product).data

        expected_data = {
            'id': 1,
            'name': 'provider_product',
            'price': 143321.13,
            'code': 574574,
            'created': provider_product.created.strftime('%Y-%m-%d'),
            'product': 1,
            'provide': 1
        }

        self.assertEqual(expected_data, data)
