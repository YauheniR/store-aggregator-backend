from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema
from drf_spectacular.utils import extend_schema_view
from rest_framework import generics
from rest_framework import filters
from rest_framework import status
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from core.exceptions import ForbiddenSerrializer
from core.exceptions import OkSerializer
from core.exceptions import BadRequestSerializer
from core.exceptions import NotFoundSerializer
from core.exceptions import MethodNotAllowedSerializer
from core.exceptions import RequestTimeoutSerializer
from core.exceptions import CreatedSerializer
from core.exceptions import NoContentSerializer
from core.filters import ProviderProductsFilter
from core.paginations import CustomPagination
from products.models import ProductModel
from products.models import ProviderProductModel
from products.serializers import ProductsSerializer
from products.serializers import ProviderProductsSerializer
from products.serializers import ProviderProductSerializer


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
            status.HTTP_403_FORBIDDEN: ForbiddenSerrializer,
            status.HTTP_404_NOT_FOUND: NotFoundSerializer,
            status.HTTP_405_METHOD_NOT_ALLOWED: MethodNotAllowedSerializer,
            status.HTTP_408_REQUEST_TIMEOUT: RequestTimeoutSerializer,
        }
    )
)
class ProductsView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = ProductModel.objects.all()
    serializer_class = ProductsSerializer
    pagination_class = CustomPagination
    ordering = 'id'


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
            status.HTTP_403_FORBIDDEN: ForbiddenSerrializer,
            status.HTTP_404_NOT_FOUND: NotFoundSerializer,
            status.HTTP_405_METHOD_NOT_ALLOWED: MethodNotAllowedSerializer,
            status.HTTP_408_REQUEST_TIMEOUT: RequestTimeoutSerializer,
        }
    ),
    patch=extend_schema(
        responses={
            status.HTTP_200_OK: OkSerializer,
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
    )
)
class ProductView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = ProductModel.objects.all()
    serializer_class = ProductsSerializer
    lookup_field = 'id'


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
            status.HTTP_403_FORBIDDEN: ForbiddenSerrializer,
            status.HTTP_404_NOT_FOUND: NotFoundSerializer,
            status.HTTP_405_METHOD_NOT_ALLOWED: MethodNotAllowedSerializer,
            status.HTTP_408_REQUEST_TIMEOUT: RequestTimeoutSerializer,
        }
    )
)
class ProviderProductsView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = ProviderProductModel.objects.all()
    serializer_class = ProviderProductsSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_class = ProviderProductsFilter
    search_fields = ('name',)
    ordering_fields = ('name', 'created',)
    pagination_class = CustomPagination
    ordering = 'id'


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
            status.HTTP_403_FORBIDDEN: ForbiddenSerrializer,
            status.HTTP_404_NOT_FOUND: NotFoundSerializer,
            status.HTTP_405_METHOD_NOT_ALLOWED: MethodNotAllowedSerializer,
            status.HTTP_408_REQUEST_TIMEOUT: RequestTimeoutSerializer,
        }
    ),
    patch=extend_schema(
        responses={
            status.HTTP_200_OK: OkSerializer,
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
    )
)
class ProviderProductView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = ProviderProductModel.objects.all()
    serializer_class = ProviderProductSerializer
    lookup_field = 'id'
