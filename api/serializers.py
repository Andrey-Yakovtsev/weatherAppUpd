import datetime

from rest_framework import serializers

from api.models import WeatherData


class WeatherDataSerializer(serializers.ModelSerializer):

    class Meta:
        model = WeatherData
        fields = '__all__'

    def create(self, validated_data):
        city, created = WeatherData.objects.update_or_create(
            city_name=validated_data.get(
                'city_name'),
                defaults={'weather_data': validated_data.get('weather_data', None)}
        )

        return city


    # def update(self, instance, validated_data):
    #     instance.city_name = validated_data.get('city_name', instance.city_name)
    #     instance.weather_data = validated_data.get('weather_data', instance.weather_data)
    #     instance.save(modified=datetime.datetime.now())
    #     return instance