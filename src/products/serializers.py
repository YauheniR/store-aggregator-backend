from rest_framework import serializers
from products.models import ProductModel
from products.models import ProviderProductModel
from providers.models import ProviderModel


class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductModel
        fields = '__all__'


class ProviderProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProviderProductModel
        fields = '__all__'

    def validate(self, attrs: dict) -> dict:
        if ProductModel.objects.filter(id=attrs['product']).exists():
            raise serializers.ValidationError('такого product не существует!')
        return attrs


class ProviderProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProviderProductModel
        fields = '__all__'

    def validate(self, attrs: dict) -> dict:
        if not ProductModel.objects.filter(id=attrs['product'].id).exists():
            raise serializers.ValidationError('такого product не существует!')

        if not ProviderModel.objects.filter(id=attrs['provide'].id).exists():
            raise serializers.ValidationError('такого provider не существует!')

        return attrs
