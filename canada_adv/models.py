from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class UserInfo(models.Model):
    user_id = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    food = models.IntegerField()
    water = models.IntegerField()
    state = models.CharField(max_length=30, blank=False)
    city = models.CharField(max_length=30, blank=False)
    location = models.CharField(max_length=30, blank=False)
    food_available = models.IntegerField(blank=False)
    water_available = models.IntegerField(blank=False)
    location_2 = models.CharField(max_length=30, blank=False)
    food_available_2 = models.IntegerField(blank=False)
    water_available_2 = models.IntegerField(blank=False)

    def __str__(self):
        return UserInfo.user_id

