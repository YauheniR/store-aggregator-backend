from rest_framework import serializers, status
from providers.models import ProviderModel


class ProviderListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProviderModel
        fields = '__all__'


class ProviderDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProviderModel
        fields = '__all__'
