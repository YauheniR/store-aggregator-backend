from rest_framework import serializers
from categories.models import CategoryModel
from categories.models import ProviderCategoryModel


class ProviderCategorySerializer(serializers.ModelSerializer):
    provider_name = serializers.ReadOnlyField(source='provider.name')

    class Meta:
        model = ProviderCategoryModel
        fields = ('url', 'provider_id', 'provider_name')


class ProviderCategoryCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProviderCategoryModel
        fields = '__all__'


class ProviderCategoryUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProviderCategoryModel
        fields = ('url',)


class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryModel
        exclude = ('position',)


class CategoryDetailSerializer(serializers.ModelSerializer):
    categories_providers = ProviderCategorySerializer(many=True)

    class Meta:
        model = CategoryModel
        fields = ('name', 'created', 'categories_providers',)
