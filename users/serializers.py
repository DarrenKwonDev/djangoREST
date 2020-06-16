from rest_framework import serializers
from . import models as users_models


class TinyUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = users_models.User
        fields = (
            "username",
            "superhost",
        )
