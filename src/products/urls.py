from django.urls import path
from django.urls import include
from products.views import ProviderProductView
from products.views import ProviderProductsView
from products.views import ProductView
from products.views import ProductsView

urlpatterns = [
    path('', ProductsView.as_view(), name='products_list'),
    path('<int:product_id>/', include(
        [
            path('', ProductView.as_view(), name='product_detail'),
            path('providers/', include(
                [
                    path('', ProviderProductsView.as_view(), name='providers_product_list'),
                    path('<int:provider_product_id>/', ProviderProductView.as_view(), name='providers_product_detail'),
                ]
            ))
        ])),
]
