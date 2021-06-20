import requests
from django.shortcuts import render
from .models import City
from .forms import CityForm

# Create your views here.
def index(request):
    api_key = '416a2e81180c6e09d4d4f248202d0b8d'

    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()

    form = CityForm()

    cities = City.objects.all()

    all_cities = []

    for city in cities:
        url = f'https://api.openweathermap.org/data/2.5/weather?q={city.name}&' \
              f'units=metric&appid={api_key}'
        res = requests.get(url).json()

        city_info = {
            'city': city.name,
            'temp': res['main']['temp'],
            'icon': res['weather'][0]['icon'],
        }
        all_cities.append(city_info)

    context = {
        'all_info': all_cities,
        'form': form,
    }

    return render(request, 'weather/index.html', context)