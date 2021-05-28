import django_filters
from providers.models import ProviderModel


class ProviderFilters(django_filters.FilterSet):
    class Meta:
        model = ProviderModel
        fields = ('name',)
