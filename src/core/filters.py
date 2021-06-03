import django_filters
from django_filters import NumberFilter
from categories.models import CategoryModel
from products.models import ProviderProductModel
from providers.models import ProviderModel


class ProviderFilter(django_filters.FilterSet):
    class Meta:
        model = ProviderModel
        fields = ('name',)


class CategoryFilter(django_filters.FilterSet):
    provider_id = NumberFilter(field_name='providercategorymodel', lookup_expr='provider_id')

    class Meta:
        model = CategoryModel
        fields = ('provider_id',)


class ProviderProductsFilter(django_filters.FilterSet):
    price__gt = NumberFilter(field_name='price', lookup_expr='gt')
    price__lt = NumberFilter(field_name='price', lookup_expr='lt')

    class Meta:
        model = ProviderProductModel
        fields = ('price__gt', 'price__lt', 'provide_id')
