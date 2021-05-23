from django.core import validators
from django.db import models
from django.urls import reverse
from django.utils.html import format_html

from products.models import ProductModel


class CategoryModel(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['name']

    def __str__(self):
        return self.name

    def display_providers_count(self):
        return ', '.join(str(ProviderCategoryModel.objects.filter(category=self).count()))

    def display_products_count(self):
        return ', '.join(str(ProductModel.objects.filter(category=self).count()))

    display_providers_count.short_description = 'Providers Count'
    display_products_count.short_description = 'Number Products'


class ProviderCategoryModel(models.Model):
    provider = models.ForeignKey('providers.ProviderModel', on_delete=models.CASCADE)
    category = models.ForeignKey('CategoryModel', on_delete=models.CASCADE)
    url = models.CharField(max_length=500, validators=[validators.URLValidator])

    class Meta:
        verbose_name = 'Provider Category'
        verbose_name_plural = 'Provider Categories'
