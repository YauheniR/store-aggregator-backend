from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema
from rest_framework import generics, filters, status
from providers.models import ProviderModel
from core.exceptions import (NotFoundSerializer,
                             BadRequestSerializer,
                             RequestTimeoutSerializer,
                             MethodNotAllowedSerializer)
from providers.serializers import (ProviderListSerializer,
                                   ProviderDetailSerializer,
                                   )


@extend_schema(
    responses={status.HTTP_404_NOT_FOUND: NotFoundSerializer,
               status.HTTP_400_BAD_REQUEST: BadRequestSerializer,
               status.HTTP_408_REQUEST_TIMEOUT: RequestTimeoutSerializer,
               status.HTTP_405_METHOD_NOT_ALLOWED: MethodNotAllowedSerializer,

               }
)
@extend_schema()
class ProvidersView(generics.ListCreateAPIView):
    queryset = ProviderModel.objects.all()
    serializer_class = ProviderListSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['name']
    ordering_fields = ['created']


@extend_schema()
class ProviderView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProviderModel.objects.all()
    serializer_class = ProviderDetailSerializer
    lookup_field = 'id'
