import django_filters
from django_filters import NumberFilter
from products.models import ProviderProductModel


class ProviderProductsFilter(django_filters.FilterSet):
    price__gt = NumberFilter(field_name='price', lookup_expr='gt')
    price__lt = NumberFilter(field_name='price', lookup_expr='lt')

    class Meta:
        model = ProviderProductModel
        fields = ('price__gt', 'price__lt', 'provide_id')
