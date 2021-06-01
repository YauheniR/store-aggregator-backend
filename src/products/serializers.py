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

    def validate(self, attrs):
        product = attrs['product']
        if ProductModel.objects.filter(id=product.id) is None:
            raise serializers.ValidationError('Product %s не существует!' % product)
        return attrs


class ProviderProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProviderProductModel
        fields = '__all__'

    def validate(self, attrs):
        product = attrs['product']
        provider = attrs['provide']
        if ProductModel.objects.filter(id=product.id) is None:
            raise serializers.ValidationError('Product %s не существует!' % product)
        if ProviderModel.objects.filter(id=provider.id) is None:
            raise serializers.ValidationError('Provider %s не существует!' % provider)
        return attrs
