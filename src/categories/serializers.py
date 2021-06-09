from rest_framework import serializers
from categories.models import CategoryModel
from categories.models import ProviderCategoryModel


class ProviderCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProviderCategoryModel
        fields = ('url', 'provider', 'category')
        read_only_field = ('provider', 'category')


class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryModel
        exclude = ('position',)


class CategorySerializer(serializers.ModelSerializer):
    categories_providers = ProviderCategorySerializer(source='providercategorymodel_set', many=True)

    class Meta:
        model = CategoryModel
        fields = ('name', 'created', 'categories_providers',)
