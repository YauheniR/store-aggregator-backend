from rest_framework import serializers


class NotFoundSerializer(serializers.Serializer):
    detail = serializers.CharField()


class BadRequestSerializer(serializers.Serializer):
    detail = serializers.CharField()


class RequestTimeoutSerializer(serializers.Serializer):
    detail = serializers.CharField()


class MethodNotAllowedSerializer(serializers.Serializer):
    detail = serializers.CharField()