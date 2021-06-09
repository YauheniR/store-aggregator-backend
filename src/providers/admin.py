from django.contrib import admin
from providers.models import ProviderModel
from products.admin import ProviderProductInstanceInLine


class ProviderAdmin(admin.ModelAdmin):
    inlines = (ProviderProductInstanceInLine,)
    list_display = ('name',)
    list_filter = ('name',)


admin.site.register(ProviderModel, ProviderAdmin)
