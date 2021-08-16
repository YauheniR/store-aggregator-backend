import django_filters
from providers.models import ProviderModel


class ProviderFilter(django_filters.FilterSet):
    class Meta:
        model = ProviderModel
        fields = ("name",)
