from rest_framework import routers
from django.urls import path, include

from api.views import WeatherDataViewSet

router = routers.DefaultRouter()
router.register('weatherapi', WeatherDataViewSet)


urlpatterns = [
    path('', include(router.urls)),
]