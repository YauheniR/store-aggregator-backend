from django.urls import path
from django.urls import include
from categories.views import ProvidersCategriesView
from categories.views import CategoriesView
from categories.views import CategoryView
from categories.views import ProviderCategoryView

urlpatterns = [
    path("", CategoriesView.as_view(), name="categories_list"),
    path(
        "<int:category_id>/",
        include(
            [
                path("", CategoryView.as_view(), name="category_detail"),
                path(
                    "providers/",
                    include(
                        [
                            path(
                                "",
                                ProvidersCategriesView.as_view(),
                                name="categories_providers_post",
                            ),
                            path(
                                "<int:provider_category_id>",
                                ProviderCategoryView.as_view(),
                                name="categories_providers_detail",
                            ),
                        ]
                    ),
                ),
            ]
        ),
    ),
]
