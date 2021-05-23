from django.contrib import admin
from .models import ProductModel, ProviderProductModel


class ProviderProductInstanceInLine(admin.TabularInline):
    model = ProviderProductModel
    extra = 0


@admin.register(ProductModel)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category_name')
    list_filter = ('name', 'category')


@admin.register(ProviderProductModel)
class ProviderProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'price', 'product')
