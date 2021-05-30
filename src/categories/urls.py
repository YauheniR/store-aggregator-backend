from django.urls import path
from django.urls import include
from categories.views import ProvidersCategriesToCategoryView
from categories.views import CategoriesView
from categories.views import CategoryView
from categories.views import ProviderCategoryToCategoryView

urlpatterns = [
    path('', CategoriesView.as_view()),
    path('<int:id>/', include(
        [
            path('', CategoryView.as_view()),
            path('providers/', include(
                [
                    path('', ProvidersCategriesToCategoryView.as_view()),
                    path('<int:id>', ProviderCategoryToCategoryView.as_view()),
                ])),
        ])),
]
