# Generated by Django 4.0 on 2021-12-25 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WeatherData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_created=True)),
                ('city_name', models.CharField(max_length=25)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('weather_data', models.JSONField()),
            ],
        ),
    ]
