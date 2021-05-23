from django.db import models
from products.models import ProductModel


class CategoryModel(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateField(auto_now_add=True)
    position = models.PositiveIntegerField(default=0, blank=False, null=False)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['position', 'name']

    def __str__(self):
        return self.name


class ProviderCategoryModel(models.Model):
    provider = models.ForeignKey('providers.ProviderModel', on_delete=models.CASCADE)
    category = models.ForeignKey('categories.CategoryModel', on_delete=models.CASCADE)
    url = models.URLField()

    class Meta:
        verbose_name = 'Provider Category'
        verbose_name_plural = 'Provider Categories'
