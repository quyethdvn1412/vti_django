from django.shortcuts import render
import requests


# Create your views here.

def index(request):
    if 'city' in request.POST and 'numberdays' in request.POST:
        city = request.POST['city']
        numbersday = request.POST['numberdays']
    else:
        city = 'Hanoi'
        numbersday = 1
    appid = '8ecb98d8e5b98d8b164515a9268010fe'
    URL = 'https://api.openweathermap.org/data/2.5/forecast/daily'
    PARAMS = {'q': city, 'cnt': numbersday, 'appid': appid, 'units': 'metric'}
    r = requests.get(url=URL, params=PARAMS)
    res = r.json()
    description = res['list']
    numbersday = res['cnt']
    return render(request, 'index.html', {'city': city, 'description': description, 'day': numbersday})