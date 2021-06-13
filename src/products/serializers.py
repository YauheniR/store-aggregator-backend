from rest_framework import serializers
from products.models import ProductModel
from products.models import ProviderProductModel


class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductModel
        fields = '__all__'


class ProviderProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProviderProductModel
        fields = '__all__'


class ProviderProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProviderProductModel
        fields = '__all__'
