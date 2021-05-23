from django.contrib import admin
from products.models import ProductModel, ProviderProductModel


class ProviderProductInstanceInLine(admin.TabularInline):
    model = ProviderProductModel
    min_num = 0
    extra = 0


class ProductAdmin(admin.ModelAdmin):
    list_display = ('category_name',)
    list_filter = ('category',)


class ProviderProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'price', 'product')


admin.site.register(ProductModel, ProductAdmin)
admin.site.register(ProviderProductModel, ProviderProductAdmin)
