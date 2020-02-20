from django.urls import path, include
from django.conf.urls import url

from . import api

from rest_framework import routers

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = routers.DefaultRouter()
router.register('userinfo', api.UserInfoViewSet)

urlpatterns = [
    path(r'', include(router.urls)),
    path("", api.UserInfoViewSet),
    path("move/", api.move_city),
    path("map/", api.map_endpoint),

    url('register/', include('rest_auth.registration.urls')),
    path('', include('rest_auth.urls')),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]
