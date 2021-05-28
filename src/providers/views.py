from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema
from rest_framework import generics
from rest_framework import status
from rest_framework import filters
from core.filters import ProviderFilters
from providers.models import ProviderModel
from core.exceptions import NotFoundSerializer
from core.exceptions import OkSerializer
from core.exceptions import BadRequestSerializer
from core.exceptions import RequestTimeoutSerializer
from core.exceptions import MethodNotAllowedSerializer
from providers.serializers import ProviderListSerializer
from providers.serializers import ProviderDetailSerializer


@extend_schema(
    responses={status.HTTP_404_NOT_FOUND: NotFoundSerializer,
               status.HTTP_400_BAD_REQUEST: BadRequestSerializer,
               status.HTTP_408_REQUEST_TIMEOUT: RequestTimeoutSerializer,
               status.HTTP_405_METHOD_NOT_ALLOWED: MethodNotAllowedSerializer,
               status.HTTP_200_OK: OkSerializer,
               }
)
class ProvidersView(generics.ListCreateAPIView):
    queryset = ProviderModel.objects.all()
    serializer_class = ProviderListSerializer
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter,)
    filterset_class = ProviderFilters
    ordering_fields = ('created',)


class ProviderView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProviderModel.objects.all()
    serializer_class = ProviderDetailSerializer
