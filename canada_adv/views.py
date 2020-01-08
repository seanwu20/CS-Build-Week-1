from .models import Player, Place

from rest_framework import viewsets
from rest_framework.response import Response

from .serializers import PlayerSerializer, PlaceSerializer
from rest_framework.decorators import action


class PlayerViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer

class PlaceViewSet(viewsets.ModelViewSet):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer
