from .models import UserData

from .utils import Map, random_generator_pick_2
from django.contrib.auth.models import User

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from .serializers import UserDataSerializer
from django.core.exceptions import ObjectDoesNotExist
from django.db.utils import IntegrityError

from rest_framework.permissions import IsAuthenticated
import random


from django.dispatch import receiver


class UserDataViewSet(viewsets.ViewSet):
    queryset = UserData.objects.all()
    serializer_class = UserDataSerializer

    permission_classes = [IsAuthenticated]

    def retrieve(self, request, *args, **kwargs):
        us_map = Map()
        us_map.populate_map()
        try:
            user_data = UserData.objects.values().get(user_id=self.kwargs['pk'])

            user = User.objects.values().get(id=self.kwargs['pk'])

            user_data['username'] = user['username']
            current_city = us_map.search_map(user_data.get('city'))
            if current_city == -1:
                return Response("Player City does not exit")
            elif current_city != -1:
                user_data['left'] = current_city.left.city if current_city.left else None
                user_data['right'] = current_city.right.city if current_city.right else None
                user_data['previous'] = current_city.previous.city if current_city.previous else None
            return Response(user_data)
        except ObjectDoesNotExist:
            return Response("Invalid user_id", status=400)


    def create(self, request, *args, **kwargs):
        places = random_generator_pick_2()
        try:
            user = User.objects.get(id=request.data.get("id"))
            UserData.objects.create(user=user, user_food=10, user_water=10, state='Florida', city="Miami",
                                    location=places[0], food_available_1=5, water_available_1=5,
                                    location_2=places[1], food_available_2=5, water_available_2=5)

            user_data = UserData.objects.values().get(user_id=request.data.get("id"))

            return Response(user_data)
        except ObjectDoesNotExist:
            return Response("User of that id does not exist", status=400)
        except IntegrityError:
            return Response("This user has already been created", status=400)

    def update(self, request, *args, **kwargs):
        # user id, next_city user chooses, food, water
        random_places = random_generator_pick_2()
        us_map = Map()
        us_map.populate_map()

        try:
            new_city = us_map.search_map(request.data.get('city'))

            user_data = UserData.objects.get(user_id=self.kwargs['pk'])

            user_data.city = new_city.city

            user_data.user_food = request.data.get('user_food')
            user_data.user_water = request.data.get('user_water')

            user_data.location = random_places[0]
            user_data.food_available_1 = random.randint(1, 10)
            user_data.water_available = random.randint(1, 10)
            user_data.state = new_city.state

            user_data.location_2 = random_places[1]
            user_data.food_available_2 = random.randint(1, 10)
            user_data.water_available_2 = random.randint(1, 10)

            user_data.save()

            player_data = UserData.objects.values().get(user_id=self.kwargs["pk"])

            left = new_city.left.city if new_city.left else None
            right = new_city.right.city if new_city.right else None
            previous = new_city.previous.city if new_city.previous else None
            player_data['left'] = left
            player_data['right'] = right
            player_data['previous'] = previous
            return Response(player_data)

        except ObjectDoesNotExist:
            return Response("Invalid User Id", status=400)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def map_endpoint(request):
    us_map = Map()
    us_map.populate_map()
    us_map_dict = us_map.to_dict(us_map.start)
    return Response(us_map_dict)
