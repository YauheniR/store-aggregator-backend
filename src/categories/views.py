from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema
from drf_spectacular.utils import extend_schema_view
from rest_framework import generics
from rest_framework import status
from categories.models import ProviderCategoryModel
from categories.models import CategoryModel
from categories.serializers import ProviderCategorySerializer
from categories.serializers import CategoriesSerializer
from categories.serializers import CategorySerializer
from core.exceptions import MethodNotAllowedSerializer, ProviderCategoryUpdateSerializer, CategoryDetailSerializer
from core.exceptions import NotFoundSerializer
from core.exceptions import BadRequestSerializer
from core.exceptions import NoContentSerializer
from core.exceptions import RequestTimeoutSerializer
from core.exceptions import OkSerializer
from core.exceptions import CreatedSerializer
from core.filters import CategoryFilter
from core.paginations import CustomPagination


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
    serializer_class = CategoriesSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = CategoryFilter
    pagination_class = CustomPagination
    ordering = 'id'


@extend_schema_view(
    get=extend_schema(
        responses={
            status.HTTP_200_OK: CategoryDetailSerializer,
            status.HTTP_400_BAD_REQUEST: BadRequestSerializer,
            status.HTTP_404_NOT_FOUND: NotFoundSerializer,
            status.HTTP_405_METHOD_NOT_ALLOWED: MethodNotAllowedSerializer,
            status.HTTP_408_REQUEST_TIMEOUT: RequestTimeoutSerializer,
        }
    ),
    put=extend_schema(
        responses={
            status.HTTP_200_OK: CategoryDetailSerializer,
            status.HTTP_400_BAD_REQUEST: BadRequestSerializer,
            status.HTTP_404_NOT_FOUND: NotFoundSerializer,
            status.HTTP_405_METHOD_NOT_ALLOWED: MethodNotAllowedSerializer,
            status.HTTP_408_REQUEST_TIMEOUT: RequestTimeoutSerializer,
        }
    ),
    patch=extend_schema(
        responses={
            status.HTTP_200_OK: CategoryDetailSerializer,
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
    serializer_class = CategorySerializer
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
class ProvidersCategriesView(generics.CreateAPIView):
    queryset = ProviderCategoryModel.objects.all()
    serializer_class = ProviderCategorySerializer


@extend_schema_view(
    get=extend_schema(
        responses={
            status.HTTP_200_OK: ProviderCategoryUpdateSerializer,
            status.HTTP_400_BAD_REQUEST: BadRequestSerializer,
            status.HTTP_404_NOT_FOUND: NotFoundSerializer,
            status.HTTP_405_METHOD_NOT_ALLOWED: MethodNotAllowedSerializer,
            status.HTTP_408_REQUEST_TIMEOUT: RequestTimeoutSerializer,
        }
    ),
    put=extend_schema(
        responses={
            status.HTTP_200_OK: ProviderCategoryUpdateSerializer,
            status.HTTP_400_BAD_REQUEST: BadRequestSerializer,
            status.HTTP_404_NOT_FOUND: NotFoundSerializer,
            status.HTTP_405_METHOD_NOT_ALLOWED: MethodNotAllowedSerializer,
            status.HTTP_408_REQUEST_TIMEOUT: RequestTimeoutSerializer,
        }
    ),
    patch=extend_schema(
        responses={
            status.HTTP_200_OK: ProviderCategoryUpdateSerializer,
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
class ProviderCategoryView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProviderCategoryModel.objects.all()
    serializer_class = ProviderCategorySerializer
    lookup_field = 'id'
