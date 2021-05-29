from django.db import models
from products.models import ProviderProductModel


class ProviderModel(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = 'Provider'
        verbose_name_plural = 'Providers'

    def __str__(self):
        return self.name
