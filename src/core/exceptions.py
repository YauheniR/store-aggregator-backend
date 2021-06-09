from rest_framework import serializers


class AbstractSerializer(serializers.Serializer):
    detail = serializers.CharField()


class NotFoundSerializer(AbstractSerializer):
    pass


class BadRequestSerializer(AbstractSerializer):
    pass


class RequestTimeoutSerializer(AbstractSerializer):
    pass


class MethodNotAllowedSerializer(AbstractSerializer):
    pass


class OkSerializer(AbstractSerializer):
    pass


class CreatedSerializer(AbstractSerializer):
    pass


class NoContentSerializer(AbstractSerializer):
    pass


class ProviderCategoryUpdateSerializer(AbstractSerializer):
    pass


class CategoryDetailSerializer(AbstractSerializer):
    pass


class ForbiddenSerrializer(AbstractSerializer):
    pass
