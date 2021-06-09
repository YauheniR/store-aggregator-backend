from django.urls import path
from django.urls import include
from products.views import ProviderProductView
from products.views import ProviderProductsView
from products.views import ProductView
from products.views import ProductsView

urlpatterns = [
    path('', ProductsView.as_view()),
    path('<int:id>/', include(
        [
            path('', ProductView.as_view()),
            path('providers/', include(
                [
                    path('', ProviderProductsView.as_view()),
                    path('<int:id>/', ProviderProductView.as_view()),
                ]
            ))
        ])),
]
