from rest_framework import serializers
from . import models as rooms_models
from users.serializers import TinyUserSerializer


class RoomSerializer(serializers.ModelSerializer):

    user = TinyUserSerializer()

    class Meta:
        model = rooms_models.Room
        fields = ("pk", "name", "price", "bedrooms", "instant_book", "user")


class BigRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = rooms_models.Room
        exclude = ()
