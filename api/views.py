from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from api.models import WeatherData
from api.serializers import WeatherDataSerializer


class WeatherDataViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows to get all WeatherData data.
    """
    queryset = WeatherData.objects.all()
    serializer_class = WeatherDataSerializer
    permission_classes = [AllowAny]