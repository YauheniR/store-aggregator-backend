from rest_framework import serializers
from providers.models import ProviderModel


class ProviderSerializers(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = ProviderModel
        fields = '__all__'
        read_only_fields = ['name']
