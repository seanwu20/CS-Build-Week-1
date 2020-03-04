from rest_framework import serializers
from .models import UserData


class UserDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserData
        fields = ['user_id', 'user_food', 'user_water',
                  'state', 'city',
                  'location', 'food_available_1', 'water_available_1',
                  'location_2', 'food_available_2', 'water_available_2']
