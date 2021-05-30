from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema
from drf_spectacular.utils import extend_schema_view
from rest_framework import generics
from rest_framework import status
from categories.models import ProviderCategoryModel
from categories.models import CategoryModel
from categories.serializers import ProviderCategoryCreateSerializer
from categories.serializers import ProviderCategoryUpdateSerializer
from categories.serializers import CategoryListSerializer
from categories.serializers import CategoryDetailSerializer
from core.exceptions import MethodNotAllowedSerializer
from core.exceptions import NotFoundSerializer
from core.exceptions import BadRequestSerializer
from core.exceptions import NoContentSerializer
from core.exceptions import RequestTimeoutSerializer
from core.exceptions import OkSerializer
from core.exceptions import CreatedSerializer
from core.filters import CategoryFilter


@extend_schema_view(
    get=extend_schema(
        responses={
            status.HTTP_200_OK: OkSerializer,
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
            status.HTTP_404_NOT_FOUND: NotFoundSerializer,
            status.HTTP_405_METHOD_NOT_ALLOWED: MethodNotAllowedSerializer,
            status.HTTP_408_REQUEST_TIMEOUT: RequestTimeoutSerializer,
        }
    )
)
class CategoriesView(generics.ListCreateAPIView):
    queryset = CategoryModel.objects.all()
    serializer_class = CategoryListSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = CategoryFilter


@extend_schema_view(
    get=extend_schema(
        responses={
            status.HTTP_200_OK: OkSerializer,
            status.HTTP_400_BAD_REQUEST: BadRequestSerializer,
            status.HTTP_404_NOT_FOUND: NotFoundSerializer,
            status.HTTP_405_METHOD_NOT_ALLOWED: MethodNotAllowedSerializer,
            status.HTTP_408_REQUEST_TIMEOUT: RequestTimeoutSerializer,
        }
    ),
    put=extend_schema(
        responses={
            status.HTTP_200_OK: OkSerializer,
            status.HTTP_400_BAD_REQUEST: BadRequestSerializer,
            status.HTTP_404_NOT_FOUND: NotFoundSerializer,
            status.HTTP_405_METHOD_NOT_ALLOWED: MethodNotAllowedSerializer,
            status.HTTP_408_REQUEST_TIMEOUT: RequestTimeoutSerializer,
        }
    ),
    patch=extend_schema(
        responses={
            status.HTTP_200_OK: OkSerializer,
            status.HTTP_400_BAD_REQUEST: BadRequestSerializer,
            status.HTTP_404_NOT_FOUND: NotFoundSerializer,
            status.HTTP_405_METHOD_NOT_ALLOWED: MethodNotAllowedSerializer,
            status.HTTP_408_REQUEST_TIMEOUT: RequestTimeoutSerializer,
        }
    ),
    delete=extend_schema(
        responses={
            status.HTTP_204_NO_CONTENT: NoContentSerializer,
            status.HTTP_400_BAD_REQUEST: BadRequestSerializer,
            status.HTTP_404_NOT_FOUND: NotFoundSerializer,
            status.HTTP_405_METHOD_NOT_ALLOWED: MethodNotAllowedSerializer,
            status.HTTP_408_REQUEST_TIMEOUT: RequestTimeoutSerializer,
        }
    )
)
class CategoryView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CategoryModel.objects.all()
    serializer_class = CategoryDetailSerializer
    lookup_field = 'id'


@extend_schema_view(
    post=extend_schema(
        responses={
            status.HTTP_201_CREATED: CreatedSerializer,
            status.HTTP_400_BAD_REQUEST: BadRequestSerializer,
            status.HTTP_404_NOT_FOUND: NotFoundSerializer,
            status.HTTP_405_METHOD_NOT_ALLOWED: MethodNotAllowedSerializer,
            status.HTTP_408_REQUEST_TIMEOUT: RequestTimeoutSerializer,
        }
    ),
)
class ProvidersCategriesToCategoryView(generics.CreateAPIView):
    queryset = ProviderCategoryModel.objects.all()
    serializer_class = ProviderCategoryCreateSerializer


@extend_schema_view(
    get=extend_schema(
        responses={
            status.HTTP_200_OK: OkSerializer,
            status.HTTP_400_BAD_REQUEST: BadRequestSerializer,
            status.HTTP_404_NOT_FOUND: NotFoundSerializer,
            status.HTTP_405_METHOD_NOT_ALLOWED: MethodNotAllowedSerializer,
            status.HTTP_408_REQUEST_TIMEOUT: RequestTimeoutSerializer,
        }
    ),
    put=extend_schema(
        responses={
            status.HTTP_200_OK: OkSerializer,
            status.HTTP_400_BAD_REQUEST: BadRequestSerializer,
            status.HTTP_404_NOT_FOUND: NotFoundSerializer,
            status.HTTP_405_METHOD_NOT_ALLOWED: MethodNotAllowedSerializer,
            status.HTTP_408_REQUEST_TIMEOUT: RequestTimeoutSerializer,
        }
    ),
    patch=extend_schema(
        responses={
            status.HTTP_200_OK: OkSerializer,
            status.HTTP_400_BAD_REQUEST: BadRequestSerializer,
            status.HTTP_404_NOT_FOUND: NotFoundSerializer,
            status.HTTP_405_METHOD_NOT_ALLOWED: MethodNotAllowedSerializer,
            status.HTTP_408_REQUEST_TIMEOUT: RequestTimeoutSerializer,
        }
    ),
    delete=extend_schema(
        responses={
            status.HTTP_204_NO_CONTENT: NoContentSerializer,
            status.HTTP_400_BAD_REQUEST: BadRequestSerializer,
            status.HTTP_404_NOT_FOUND: NotFoundSerializer,
            status.HTTP_405_METHOD_NOT_ALLOWED: MethodNotAllowedSerializer,
            status.HTTP_408_REQUEST_TIMEOUT: RequestTimeoutSerializer,
        }
    )
)
class ProviderCategoryToCategoryView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProviderCategoryModel.objects.all()
    serializer_class = ProviderCategoryUpdateSerializer
    lookup_field = 'id'
