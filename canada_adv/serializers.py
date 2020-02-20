from rest_framework import serializers
from .models import UserInfo


class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        fields = ['user_id', 'food', 'water',
                  'state', 'city',
                  'location', 'food_available', 'water_available',
                  'location_2', 'food_available_2', 'water_available_2']
