from rest_framework.decorators import api_view
from rest_framework.response import Response
from . import models as rooms_models
from .serializers import RoomSerializer


@api_view(["GET"])
def list_rooms(request):

    rooms = rooms_models.Room.objects.all()
    serialized_rooms = RoomSerializer(rooms, many=True)

    return Response(data=serialized_rooms.data)
