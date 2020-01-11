from django.db import models


# Create your models here.


class Player(models.Model):
    email = models.EmailField()
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
        return "Player email:" + self.email + ", Current City:" + self.city + " Current State:" + self.state

