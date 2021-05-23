from django.contrib import admin
from .models import ProviderModel
from products.admin import ProviderProductInstanceInLine


@admin.register(ProviderModel)
class ProviderAdmin(admin.ModelAdmin):
    inlines = [ProviderProductInstanceInLine]
    list_display = ('name', 'display_products_count')
    list_filter = ('name',)
