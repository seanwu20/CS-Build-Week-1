from django.urls import path, include
from django.conf.urls import url

from . import api

from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = routers.DefaultRouter()
router.register('userinfo', api.UserInfoViewSet)

urlpatterns = [
    url('register/', include('rest_auth.registration.urls')),
    url('', include('rest_auth.urls')),
    path('token-auth/', obtain_auth_token, name='api_token_auth'),

    # path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path(r'', include(router.urls)),

    path("map/", api.map_endpoint),

]
