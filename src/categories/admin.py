from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from products.models import ProductModel
from categories.models import ProviderCategoryModel
from categories.models import CategoryModel
from adminsortable2.admin import SortableAdminMixin


class ProviderCategoryInstanceInLine(admin.TabularInline):
    model = ProviderCategoryModel
    min_num = 1
    extra = 0


class ProviderCategoryAdmin(admin.ModelAdmin):
    list_display = ('provider', 'url')


class CategoryAdmin(SortableAdminMixin, admin.ModelAdmin):
    inlines = (ProviderCategoryInstanceInLine,)
    list_display = ('name', 'display_providers_count', 'display_products_count', 'display_button')

    def display_providers_count(self, obj: CategoryModel) -> int:
        return ProviderCategoryModel.objects.filter(category=obj).count()

    def display_products_count(self, obj: CategoryModel) -> int:
        return ProductModel.objects.filter(category=obj).count()

    def display_button(self, obj: CategoryModel) -> format_html:
        return format_html('<a class="button" href="{}?category__id__exact=%s">Button</a>' % (obj.id,),
                           reverse('admin:%s_%s_changelist' % (
                               ProductModel._meta.app_label, ProductModel._meta.model_name), ))

    display_button.short_description = 'This Products'
    display_button.allow_tags = True
    display_providers_count.short_description = 'Providers Count'
    display_products_count.short_description = 'Number Products'


admin.site.register(ProviderCategoryModel, ProviderCategoryAdmin)
admin.site.register(CategoryModel, CategoryAdmin, )
