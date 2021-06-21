from rest_framework import serializers
from products.models import ProductModel
from products.models import ProviderProductModel
from products.tasks import find_provider_product_id


class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductModel
        fields = '__all__'


class ProviderProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProviderProductModel
        fields = '__all__'

    def create(self, validated_data: dict) -> serializers.ModelSerializer:
        instance = super().create(validated_data)
        find_provider_product_id.delay(instance.id)
        return instance


class ProviderProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProviderProductModel
        fields = '__all__'
