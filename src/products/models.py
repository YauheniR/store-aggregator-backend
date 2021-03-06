from django.core import validators
from django.db import models


class ProductModel(models.Model):
    category = models.ForeignKey("categories.CategoryModel", on_delete=models.CASCADE)
    created = models.DateField(auto_now_add=True)

    def category_name(self) -> str:
        return self.category.name

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"


class ProviderProductModel(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField(
        validators=[validators.MinValueValidator(0)],
    )
    code = models.IntegerField(
        validators=[validators.MinValueValidator(0)],
    )
    product = models.ForeignKey("products.ProductModel", on_delete=models.CASCADE)
    provide = models.ForeignKey("providers.ProviderModel", on_delete=models.CASCADE)
    created = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = "Provider Product"
        verbose_name_plural = "Provider Products"
