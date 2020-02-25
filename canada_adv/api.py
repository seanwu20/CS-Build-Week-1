from .models import UserInfo

from .utils import Map, random_generator_pick_2

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from .serializers import UserInfoSerializer
from django.core.exceptions import ObjectDoesNotExist

from rest_framework.permissions import IsAuthenticated
import random


class UserInfoViewSet(viewsets.ModelViewSet):
    queryset = UserInfo.objects.all()
    serializer_class = UserInfoSerializer
    permission_classes = [IsAuthenticated]

    def retrieve(self, request, *args, **kwargs):
        us_map = Map()
        us_map.populate_map()
        try:
            user_data = UserInfo.objects.values().get(user_id=self.kwargs['pk'])
            current_city = us_map.search_map(user_data.get('city'))
            if current_city == -1:
                return Response("Player City does not exit")
            elif current_city != -1:
                user_data['left'] = current_city.left.city if current_city.left else None
                user_data['right'] = current_city.right.city if current_city.right else None
                user_data['previous'] = current_city.previous.city if current_city.previous else None
            return Response(user_data)
        except ObjectDoesNotExist:
            return Response("Invalid user_id")

    def update(self, request, *args, **kwargs):
        # user id, next_city user chooses, food, water
        random_places = random_generator_pick_2()

        us_map = Map()
        us_map.populate_map()
        try:
            new_city = us_map.search_map(request.data.get('new_city'))

            user_data = UserInfo.objects.get(user_id=self.kwargs['pk'])

            user_data.city = new_city.city

            user_data.user_food = request.data.get('user_food')
            user_data.user_water = request.data.get('user_water')

            user_data.location = random_places[0]
            user_data.food_available = random.randint(1, 10)
            user_data.water_available = random.randint(1, 10)
            user_data.state = new_city.state

            user_data.location_2 = random_places[1]
            user_data.food_available_2 = random.randint(1, 10)
            user_data.water_available_2 = random.randint(1, 10)

            user_data.save()

            player_data = UserInfo.objects.values().get(user_id=self.kwargs['pk'])

            left = new_city.left.city if new_city.left else None
            right = new_city.right.city if new_city.right else None
            previous = new_city.previous.city if new_city.previous else None
            player_data['left'] = left
            player_data['right'] = right
            player_data['previous'] = previous
            return Response(player_data)

        except ObjectDoesNotExist:
            return Response("Invalid User Id")


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def map_endpoint(request):
    us_map = Map()
    us_map.populate_map()
    us_map_dict = us_map.to_dict(us_map.start)
    return Response(us_map_dict)
