from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from categories.models import CategoryModel
from products.models import ProductModel
from products.models import ProviderProductModel
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


class ProductApiTestCase(UserRegistration):
    data = None
    detail_data = None
    category = None

    def setUp(self) -> None:
        super().setUp()

        CategoryModel.objects.bulk_create(
            [
                CategoryModel(name="category 1"),
                CategoryModel(name="category 2"),
                CategoryModel(name="category 3"),
            ]
        )
        self.category = CategoryModel.objects.get(name="category 1")

        self.data = ProductModel.objects.bulk_create(
            [ProductModel(category=self.category), ProductModel(category=self.category)]
        )
        self.detail_data = self.data[0]

    def test_get_products_call_200_ok(self) -> None:
        response = self.client.get(reverse("products_list"))

        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(ProductModel.objects.count(), len(self.data))

    def test_get_product_call_200_ok(self):
        response = self.client.get(
            reverse("product_detail", args=(self.detail_data.id,))
        )

        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(response.data.get("category"), self.detail_data.category.id)
        self.assertEqual(
            response.data.get("created"), self.detail_data.created.strftime("%Y-%m-%d")
        )

    def test_post_product_call_201_created(self):
        response = self.client.post(
            reverse("products_list"), {"category": self.category.id}
        )

        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        self.assertEqual(self.category.id, response.data.get("category"))

    def test_put_product_call_200_ok(self):
        put_category = CategoryModel.objects.get(name="category 2")
        response = self.client.put(
            reverse("product_detail", args=(self.detail_data.id,)),
            {"category": put_category.id},
        )

        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(put_category.id, response.data.get("category"))

    def test_patch_product_call_200_ok(self):
        patch_category = CategoryModel.objects.get(name="category 3")
        response = self.client.patch(
            reverse("product_detail", args=(self.detail_data.id,)),
            {"category": patch_category.id},
        )

        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(patch_category.id, response.data.get("category"))

    def test_delete_product_call_204_no_content(self):
        response = self.client.delete(
            reverse("product_detail", args=(self.detail_data.id,))
        )

        self.assertEqual(status.HTTP_204_NO_CONTENT, response.status_code)


class ProviderProductApiTestCase(UserRegistration):
    detail_data = None
    data = None
    product = None
    provide = None

    def setUp(self) -> None:
        super().setUp()

        category = CategoryModel.objects.create(name="Category")
        provider = ProviderModel.objects.create(name="Provider")
        product = ProductModel.objects.create(category=category)
        self.provide = provider
        self.product = product
        self.data = ProviderProductModel.objects.bulk_create(
            [
                ProviderProductModel(
                    name="provider product 1",
                    price=25.23,
                    code=32543465,
                    provide=provider,
                    product=product,
                ),
                ProviderProductModel(
                    name="provider product 2",
                    price=55.48,
                    code=32543345,
                    provide=provider,
                    product=product,
                ),
            ]
        )
        self.detail_data = self.data[0]

    def test_get_provider_products_call_200_ok(self):
        response = self.client.get(
            reverse("providers_product_list", args=(self.product.id,))
        )

        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(ProviderProductModel.objects.count(), len(self.data))

    def test_get_provider_product_call_200_ok(self):
        response = self.client.get(
            reverse(
                "providers_product_detail", args=(self.product.id, self.detail_data.id)
            )
        )

        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(self.detail_data.name, response.data.get("name"))
        self.assertEqual(self.detail_data.price, response.data.get("price"))
        self.assertEqual(self.detail_data.code, response.data.get("code"))

    def test_post_provider_product_call_201_created(self):
        post_provider_product = ProviderProductModel(
            name="tmpName",
            price=235.235,
            code=32526,
            product=self.product,
            provide=self.provide,
        )

        response = self.client.post(
            reverse("providers_product_list", args=(self.product.id,)),
            {
                "name": post_provider_product.name,
                "price": post_provider_product.price,
                "code": post_provider_product.code,
                "product": post_provider_product.product.id,
                "provide": post_provider_product.provide.id,
            },
        )

        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        self.assertEqual(response.data.get("name"), post_provider_product.name)
        self.assertEqual(response.data.get("price"), post_provider_product.price)
        self.assertEqual(response.data.get("code"), post_provider_product.code)

    def test_put_provider_product_call_200_ok(self):
        put_provider_product = ProviderProductModel(
            name="New Name",
            price=6457457,
            code=23523464,
            product=self.product,
            provide=self.provide,
        )

        response = self.client.put(
            reverse(
                "providers_product_detail", args=(self.product.id, self.detail_data.id)
            ),
            {
                "name": put_provider_product.name,
                "price": put_provider_product.price,
                "code": put_provider_product.code,
                "product": put_provider_product.product.id,
                "provide": put_provider_product.provide.id,
            },
        )

        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(response.data.get("name"), put_provider_product.name)
        self.assertEqual(response.data.get("price"), put_provider_product.price)
        self.assertEqual(response.data.get("code"), put_provider_product.code)

    def test_patch_provider_product_call_200_ok(self):
        patch_provider_product = ProviderProductModel(
            name="Patch Name",
            price=684734635,
            code=1241325423,
            product=self.product,
            provide=self.provide,
        )

        response = self.client.patch(
            reverse(
                "providers_product_detail", args=(self.product.id, self.detail_data.id)
            ),
            {
                "name": patch_provider_product.name,
                "price": patch_provider_product.price,
                "code": patch_provider_product.code,
                "product": patch_provider_product.product.id,
                "provide": patch_provider_product.provide.id,
            },
        )

        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(response.data.get("name"), patch_provider_product.name)
        self.assertEqual(response.data.get("price"), patch_provider_product.price)
        self.assertEqual(response.data.get("code"), patch_provider_product.code)

    def test_delete_provider_product_call_201_no_content(self):
        response = self.client.delete(
            reverse(
                "providers_product_detail",
                args=(
                    self.product.id,
                    self.detail_data.id,
                ),
            )
        )

        self.assertEqual(status.HTTP_204_NO_CONTENT, response.status_code)
