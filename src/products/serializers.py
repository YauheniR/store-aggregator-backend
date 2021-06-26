from rest_framework import serializers
from products.models import ProductModel
from products.models import ProviderProductModel
from products.tasks import find_id_from_provider_product


class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductModel
        fields = '__all__'


class ProviderProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProviderProductModel
        fields = '__all__'


class ProviderProductSerializer(serializers.ModelSerializer):
    def create(self, validated_data: dict) -> ProviderProductModel:
        instance = super().create(validated_data)
        find_id_from_provider_product.delay(instance.id)
        return instance

    class Meta:
        model = ProviderProductModel
        fields = '__all__'
