from rest_framework import serializers
from users.models import UserModel


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = (
            'username', 'last_name',
            'first_name', 'email',
            'city', 'address',
            'language', 'date_of_birth',
        )
