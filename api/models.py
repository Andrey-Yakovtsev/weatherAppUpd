from django.db import models

class WeatherData(models.Model):
    city_name = models.CharField(blank=False, null=False, max_length=25)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    weather_data = models.JSONField()
