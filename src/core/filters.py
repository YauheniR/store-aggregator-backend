import django_filters
from django_filters import NumberFilter
from categories.models import CategoryModel
from providers.models import ProviderModel


class ProviderFilter(django_filters.FilterSet):
    class Meta:
        model = ProviderModel
        fields = ('name',)


class CategoryFilter(django_filters.FilterSet):
    provider_id = NumberFilter(field_name='categories_providers', lookup_expr='provider_id')

    class Meta:
        model = CategoryModel
        fields = ('provider_id',)
