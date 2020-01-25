import requests
from django.shortcuts import render
from .models import City

def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&APPID=f4624920362748e4918830360342e0fc'
    city = 'Sarajevo'

    cities = City.objects.all()

    weather_data = []

    for city in cities:
        response = requests.get(url.format(city)).json()

        city_weather = {
            'city':city.name, 
            'temperature': response['main']['temp'],
            'description': response['weather'][0]['description'],
            'icon': response['weather'][0]['icon']
        }

        weather_data.append(city_weather)


    context = {'weather_data': weather_data}

    return render(request, 'weather/weather.html', context)
# Create your views here.
