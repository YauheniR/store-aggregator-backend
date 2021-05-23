from django.conf.urls import url
from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from products.models import ProductModel
from .models import ProviderCategoryModel
from .models import CategoryModel


class ProviderCategoryInstanceInLine(admin.TabularInline):
    model = ProviderCategoryModel
    extra = 0


@admin.register(ProviderCategoryModel)
class ProviderCategoryAdmin(admin.ModelAdmin):
    list_display = ('provider', 'url')


@admin.register(CategoryModel)
class CategoryAdmin(admin.ModelAdmin):
    inlines = [ProviderCategoryInstanceInLine]
    list_display = ('name', 'display_providers_count', 'display_products_count', 'display_button')

    def display_button(self, obj):
        return format_html('<a class="button" href="{}?category__id__exact=%s">Button</a>' % (obj.id,),
                           reverse('admin:%s_%s_changelist' % (ProductModel._meta.app_label,  ProductModel._meta.model_name),))

    display_button.short_description = 'This Products'
    display_button.allow_tags = True
