from .models import UserInfo

from .utils import Map, random_generator_pick_2

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import UserInfoSerializer
from django.core.exceptions import ObjectDoesNotExist

import random


class UserInfoViewSet(viewsets.ModelViewSet):
    queryset = UserInfo.objects.all()
    serializer_class = UserInfoSerializer


@api_view(["POST"])
def player_info(request):
    us_map = Map()
    us_map.populate_map()
    try:
        player_data = UserInfo.objects.values().get(email=request.data.get('email'))
        current_city = us_map.search_map(player_data.get('city'))
        if current_city == -1:
            return Response("Player City does not exit")
        elif current_city != -1:
            player_data['left'] = current_city.left.city if current_city.left else None
            player_data['right'] = current_city.right.city if current_city.right else None
            player_data['previous'] = current_city.previous.city if current_city.previous else None
        return Response(player_data)
    except ObjectDoesNotExist:
        return Response("Invalid email")


@api_view(["PUT"])
def move_city(request):
    # user id, next_city user chooses, food, water
    random_places = random_generator_pick_2()

    us_map = Map()
    us_map.populate_map()
    try:
        new_city = us_map.search_map(request.data.get('new_city'))

        left = new_city.left.city if new_city.left else None
        right = new_city.right.city if new_city.right else None
        previous = new_city.previous.city if new_city.previous else None

        player = UserInfo.objects.get(user_id=request.data.get('user_id'))
        player.city = request.data.get('new_city')
        player.food = request.data.get('food')
        player.water = request.data.get('water')

        player.location = random_places[0]
        player.food_available = random.randint(1, 10)
        player.water_available = random.randint(1, 10)
        player.state = new_city.state

        player.location_2 = random_places[1]
        player.food_available_2 = random.randint(1, 10)
        player.water_available_2 = random.randint(1, 10)

        player.save()

        player_data = UserInfo.objects.values().get(user_id=request.data.get('user_id'))

        player_data['left'] = left
        player_data['right'] = right
        player_data['previous'] = previous

        return Response(player_data)

    except ObjectDoesNotExist:
        return Response("Invalid User Id")


@api_view(["GET"])
def map_endpoint(request):
    us_map = Map()
    us_map.populate_map()
    us_map_dict = us_map.to_dict(us_map.start)
    return Response(us_map_dict)
