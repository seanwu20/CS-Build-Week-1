from django.urls import path, include
from django.conf.urls import url
from . import api
from rest_framework import routers

router = routers.SimpleRouter()
router.register('userdata', api.UserDataViewSet)

urlpatterns = [
    url('register/', include('rest_auth.registration.urls')),
    url('', include('rest_auth.urls')),
    path(r'', include(router.urls)),
    path("map/", api.map_endpoint),

]
