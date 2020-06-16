from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from . import models as rooms_models
from .serializers import RoomSerializer, BigRoomSerializer


class ListRoomsView(ListAPIView):

    queryset = rooms_models.Room.objects.all()
    serializer_class = RoomSerializer


class SeeRoomView(RetrieveAPIView):

    queryset = rooms_models.Room.objects.all()
    serializer_class = BigRoomSerializer
