from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema
from drf_spectacular.utils import extend_schema_view
from rest_framework import generics
from rest_framework import status
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from categories.filters import CategoryFilter
from categories.models import ProviderCategoryModel
from categories.models import CategoryModel
from categories.serializers import ProviderCategorySerializer
from categories.serializers import CategoriesSerializer
from categories.serializers import CategorySerializer
from core.exceptions import ForbiddenSerrializer
from core.exceptions import MethodNotAllowedSerializer
from core.exceptions import NotFoundSerializer
from core.exceptions import BadRequestSerializer
from core.exceptions import NoContentSerializer
from core.exceptions import RequestTimeoutSerializer
from core.exceptions import CreatedSerializer
from core.paginations import CustomPagination


@extend_schema_view(
    get=extend_schema(
        responses={
            status.HTTP_200_OK: CategoriesSerializer,
            status.HTTP_400_BAD_REQUEST: BadRequestSerializer,
            status.HTTP_404_NOT_FOUND: NotFoundSerializer,
            status.HTTP_405_METHOD_NOT_ALLOWED: MethodNotAllowedSerializer,
            status.HTTP_408_REQUEST_TIMEOUT: RequestTimeoutSerializer,
        }
    ),
    post=extend_schema(
        responses={
            status.HTTP_201_CREATED: CreatedSerializer,
            status.HTTP_400_BAD_REQUEST: BadRequestSerializer,
            status.HTTP_403_FORBIDDEN: ForbiddenSerrializer,
            status.HTTP_404_NOT_FOUND: NotFoundSerializer,
            status.HTTP_405_METHOD_NOT_ALLOWED: MethodNotAllowedSerializer,
            status.HTTP_408_REQUEST_TIMEOUT: RequestTimeoutSerializer,
        }
    ),
)
class CategoriesView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = CategoryModel.objects.all()
    serializer_class = CategoriesSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = CategoryFilter
    pagination_class = CustomPagination
    ordering = "id"


@extend_schema_view(
    get=extend_schema(
        responses={
            status.HTTP_200_OK: CategorySerializer,
            status.HTTP_400_BAD_REQUEST: BadRequestSerializer,
            status.HTTP_404_NOT_FOUND: NotFoundSerializer,
            status.HTTP_405_METHOD_NOT_ALLOWED: MethodNotAllowedSerializer,
            status.HTTP_408_REQUEST_TIMEOUT: RequestTimeoutSerializer,
        }
    ),
    put=extend_schema(
        responses={
            status.HTTP_200_OK: CategorySerializer,
            status.HTTP_400_BAD_REQUEST: BadRequestSerializer,
            status.HTTP_403_FORBIDDEN: ForbiddenSerrializer,
            status.HTTP_404_NOT_FOUND: NotFoundSerializer,
            status.HTTP_405_METHOD_NOT_ALLOWED: MethodNotAllowedSerializer,
            status.HTTP_408_REQUEST_TIMEOUT: RequestTimeoutSerializer,
        }
    ),
    patch=extend_schema(
        responses={
            status.HTTP_200_OK: CategorySerializer,
            status.HTTP_400_BAD_REQUEST: BadRequestSerializer,
            status.HTTP_403_FORBIDDEN: ForbiddenSerrializer,
            status.HTTP_404_NOT_FOUND: NotFoundSerializer,
            status.HTTP_405_METHOD_NOT_ALLOWED: MethodNotAllowedSerializer,
            status.HTTP_408_REQUEST_TIMEOUT: RequestTimeoutSerializer,
        }
    ),
    delete=extend_schema(
        responses={
            status.HTTP_204_NO_CONTENT: NoContentSerializer,
            status.HTTP_400_BAD_REQUEST: BadRequestSerializer,
            status.HTTP_403_FORBIDDEN: ForbiddenSerrializer,
            status.HTTP_404_NOT_FOUND: NotFoundSerializer,
            status.HTTP_405_METHOD_NOT_ALLOWED: MethodNotAllowedSerializer,
            status.HTTP_408_REQUEST_TIMEOUT: RequestTimeoutSerializer,
        }
    ),
)
class CategoryView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = CategoryModel.objects.all()
    serializer_class = CategorySerializer
    lookup_field = "id"
    lookup_url_kwarg = "category_id"


@extend_schema_view(
    post=extend_schema(
        responses={
            status.HTTP_201_CREATED: CreatedSerializer,
            status.HTTP_400_BAD_REQUEST: BadRequestSerializer,
            status.HTTP_403_FORBIDDEN: ForbiddenSerrializer,
            status.HTTP_404_NOT_FOUND: NotFoundSerializer,
            status.HTTP_405_METHOD_NOT_ALLOWED: MethodNotAllowedSerializer,
            status.HTTP_408_REQUEST_TIMEOUT: RequestTimeoutSerializer,
        }
    ),
)
class ProvidersCategriesView(generics.CreateAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = ProviderCategoryModel.objects.all()
    serializer_class = ProviderCategorySerializer


@extend_schema_view(
    get=extend_schema(
        responses={
            status.HTTP_200_OK: ProviderCategorySerializer,
            status.HTTP_400_BAD_REQUEST: BadRequestSerializer,
            status.HTTP_404_NOT_FOUND: NotFoundSerializer,
            status.HTTP_405_METHOD_NOT_ALLOWED: MethodNotAllowedSerializer,
            status.HTTP_408_REQUEST_TIMEOUT: RequestTimeoutSerializer,
        }
    ),
    put=extend_schema(
        responses={
            status.HTTP_200_OK: ProviderCategorySerializer,
            status.HTTP_400_BAD_REQUEST: BadRequestSerializer,
            status.HTTP_403_FORBIDDEN: ForbiddenSerrializer,
            status.HTTP_404_NOT_FOUND: NotFoundSerializer,
            status.HTTP_405_METHOD_NOT_ALLOWED: MethodNotAllowedSerializer,
            status.HTTP_408_REQUEST_TIMEOUT: RequestTimeoutSerializer,
        }
    ),
    patch=extend_schema(
        responses={
            status.HTTP_200_OK: ProviderCategorySerializer,
            status.HTTP_400_BAD_REQUEST: BadRequestSerializer,
            status.HTTP_403_FORBIDDEN: ForbiddenSerrializer,
            status.HTTP_404_NOT_FOUND: NotFoundSerializer,
            status.HTTP_405_METHOD_NOT_ALLOWED: MethodNotAllowedSerializer,
            status.HTTP_408_REQUEST_TIMEOUT: RequestTimeoutSerializer,
        }
    ),
    delete=extend_schema(
        responses={
            status.HTTP_204_NO_CONTENT: NoContentSerializer,
            status.HTTP_400_BAD_REQUEST: BadRequestSerializer,
            status.HTTP_403_FORBIDDEN: ForbiddenSerrializer,
            status.HTTP_404_NOT_FOUND: NotFoundSerializer,
            status.HTTP_405_METHOD_NOT_ALLOWED: MethodNotAllowedSerializer,
            status.HTTP_408_REQUEST_TIMEOUT: RequestTimeoutSerializer,
        }
    ),
)
class ProviderCategoryView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = ProviderCategoryModel.objects.all()
    serializer_class = ProviderCategorySerializer
    lookup_field = "id"
    lookup_url_kwarg = "provider_category_id"

    def get_queryset(self):
        return (
            super(ProviderCategoryView, self)
            .get_queryset()
            .filter(category_id=self.kwargs.get("category_id"))
        )
