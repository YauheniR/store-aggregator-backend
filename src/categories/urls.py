from django.urls import path
from django.urls import include
from categories.views import ProvidersCategriesView
from categories.views import CategoriesView
from categories.views import CategoryView
from categories.views import ProviderCategoryView

urlpatterns = [
    path('', CategoriesView.as_view()),
    path('<int:id>/', include(
        [
            path('', CategoryView.as_view()),
            path('providers/', include(
                [
                    path('', ProvidersCategriesView.as_view()),
                    path('<int:id>', ProviderCategoryView.as_view()),
                ])),
        ])),
]
