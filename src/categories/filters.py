import django_filters
from django_filters import NumberFilter
from categories.models import CategoryModel


class CategoryFilter(django_filters.FilterSet):
    provider_id = NumberFilter(
        field_name="providercategorymodel", lookup_expr="provider_id"
    )

    class Meta:
        model = CategoryModel
        fields = ("provider_id",)
