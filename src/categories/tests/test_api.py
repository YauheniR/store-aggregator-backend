from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from categories.models import CategoryModel
from categories.models import ProviderCategoryModel
from providers.models import ProviderModel


class UserRegistration(APITestCase):
    _user_data_ = {
        "username": "test_user",
        "email": "test@localhost.app",
        "password1": "strongPassword",
        "password2": "strongPassword",
    }

    def setUp(self) -> None:
        self.client.post("/api/rest-auth/registration/", self._user_data_)


class CategoriesApiTestCase(UserRegistration):
    data = None
    detail_data = None

    def setUp(self) -> None:
        super().setUp()
        self.data = CategoryModel.objects.bulk_create(
            [
                CategoryModel(name="Category 1"),
                CategoryModel(name="Category 2"),
                CategoryModel(name="Category 3"),
                CategoryModel(name="Category 4"),
            ]
        )

        self.detail_data = CategoryModel.objects.get(name="Category 1")

    def test_get_categories_call_200_ok(self):
        response = self.client.get(reverse("categories_list"))

        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(CategoryModel.objects.count(), len(self.data))

    def test_get_category_call_200_ok(self):
        response = self.client.get(
            reverse("category_detail", args=(self.detail_data.id,))
        )

        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(response.data.get("name"), self.detail_data.name)
        self.assertEqual(
            response.data.get("created"), self.detail_data.created.strftime("%Y-%m-%d")
        )

    def test_post_category_call_201_created(self):
        response = self.client.post(reverse("categories_list"), {"name": "tmpName"})
        new_category = CategoryModel.objects.get(name="tmpName")

        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        self.assertEqual(response.data.get("name"), new_category.name)
        self.assertEqual(
            response.data.get("created"), new_category.created.strftime("%Y-%m-%d")
        )

    def test_put_category_call_200_ok(self):
        response = self.client.put(
            reverse("category_detail", args=(self.detail_data.id,)),
            {"name": "New Name"},
        )
        put_category = CategoryModel.objects.get(name="New Name")

        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(response.data.get("name"), put_category.name)
        self.assertEqual(
            response.data.get("created"), put_category.created.strftime("%Y-%m-%d")
        )

    def test_patch_category_call_200_ok(self):
        response = self.client.patch(
            reverse("category_detail", args=(self.detail_data.id,)),
            {"name": "Some Name"},
        )
        patch_category = CategoryModel.objects.get(name="Some Name")

        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(response.data.get("name"), patch_category.name)
        self.assertEqual(
            response.data.get("created"), patch_category.created.strftime("%Y-%m-%d")
        )

    def test_delete_category_call_204_no_content(self):
        response = self.client.delete(
            reverse("category_detail", args=(self.detail_data.id,))
        )

        self.assertEqual(status.HTTP_204_NO_CONTENT, response.status_code)


class ProviderCategoriesApiTestCase(UserRegistration):
    provider = None
    category = None
    detail_data = None
    url_provider_category = "https://www.google.by/"

    def setUp(self) -> None:
        super().setUp()

        self.provider = ProviderModel.objects.create(name="Provider")
        self.category = CategoryModel.objects.create(name="Category")
        ProviderCategoryModel.objects.create(
            url=self.url_provider_category,
            category=self.category,
            provider=self.provider,
        )

        self.detail_data = ProviderCategoryModel.objects.get(
            url=self.url_provider_category
        )

    def test_get_provider_category_call_200_ok(self):
        response = self.client.get(
            reverse(
                "categories_providers_detail",
                args=(self.category.id, self.detail_data.id),
            )
        )

        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(self.detail_data.url, response.data["url"])
        self.assertEqual(self.detail_data.provider_id, response.data["provider"])
        self.assertEqual(self.detail_data.category_id, response.data["category"])

    def test_post_provider_category_call_201_created(self):
        new_url = "https://github.com"
        response = self.client.post(
            reverse("categories_providers_post", args=(self.category.id,)),
            {
                "url": new_url,
                "provider": self.provider.id,
                "category": self.category.id,
            },
        )

        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        self.assertEqual(new_url, response.data.get("url"))

    def test_put_provider_category_call_200_ok(self):
        put_url = "https://www.youtube.com"
        response = self.client.put(
            reverse(
                "categories_providers_detail",
                args=(
                    self.category.id,
                    self.detail_data.id,
                ),
            ),
            {
                "url": put_url,
                "provider": self.provider.id,
                "category": self.category.id,
            },
        )

        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(put_url, response.data.get("url"))

    def test_patch_provider_category_call_200_ok(self):
        patch_url = "https://stackoverflow.com"
        response = self.client.patch(
            reverse(
                "categories_providers_detail",
                args=(
                    self.category.id,
                    self.detail_data.id,
                ),
            ),
            {
                "url": patch_url,
                "provider": self.provider.id,
                "category": self.category.id,
            },
        )

        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(patch_url, response.data.get("url"))

    def test_delete_provider_category_call_204_no_content(self):
        response = self.client.delete(
            reverse(
                "categories_providers_detail",
                args=(
                    self.category.id,
                    self.detail_data.id,
                ),
            )
        )

        self.assertEqual(status.HTTP_204_NO_CONTENT, response.status_code)
