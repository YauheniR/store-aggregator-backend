from celery import shared_task
from categories.models import ProviderCategoryModel


@shared_task
def get_provider_category() -> int:
    providers_category = ProviderCategoryModel.objects.all()
    return providers_category.count()
