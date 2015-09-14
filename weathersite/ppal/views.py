from django.shortcuts import render

from django.http import *

from django.core.urlresolvers import reverse,reverse_lazy


from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required


from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render
from django.core.urlresolvers import reverse,reverse_lazy
from django.http import *
from ppal.forms import *
from ppal.models import *
from datetime import datetime, timedelta, time
import json
from django.http import HttpResponse
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login')
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse(show_city_today))

def user_login(request):
    if not request.user.is_anonymous():
        return HttpResponseRedirect(reverse(show_city_today))
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        if form.is_valid:
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                dest = request.GET.get('next') if request.GET.get('next') != None else reverse(show_city_today)
                return HttpResponseRedirect(dest)
            else:
                return HttpResponse('not valid username or password')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def create_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            u = authenticate(username=request.POST['username'],
                             password=request.POST['password'])
            login(request, u)
            return HttpResponseRedirect(reverse(show_city_today))
        else:
            return HttpResponse('user not valid')
    else:
        form = UserForm()
    return render(request, 'user_form.html', {'form': form})


@login_required(login_url='/login')
def create_city(request):
    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            city = form.save()
            return HttpResponseRedirect(reverse(show_city_today))
    else:
        form = CityForm()
    return render(request, 'city_form.html', {'form': form})

@login_required(login_url='/login')
def create_daily_weather(request, pk):
    if request.method == 'POST':
        form = WeatherForm(request.POST)
        if form.is_valid():
            weather = form.save(commit = False)
            weather.city = City.objects.get(id=pk)
            weather.save()
            return HttpResponseRedirect(reverse(show_daily_temperatures,kwargs={'num':pk}))
    else:
        form = WeatherForm()
    return render(request, 'weather_form.html', {'form': form})

def show_city_today(request):
    all_cities = City.objects.filter()
    city_list = DailyWeather.objects.filter(day=datetime.now().date())
    return render(request, 'show_cities.html', {
        'city_list': city_list,
        'all_cities': all_cities,

    })

def show_daily_temperatures(request,num):
	temperatures_list = DailyWeather.objects.filter(city=num).order_by('-day')

	return render(request, 'show_city_temperature.html', {
		'temperatures_list': temperatures_list,
        'city': City.objects.get(id=num),
	})

def api_info(request):
    all_cities = City.objects.filter()
    return render(request, 'api_info.html', {
        'all_cities': all_cities,
    })

def json_api_temperature(request, city):
    if City.objects.filter(name=city):
        list = DailyWeather.objects.filter(city=City.objects.filter(name=city).order_by('-day'))
        temp = list[0].temperature
        date = list[0].day
        data = {'city': city,'date':str(date), 'temp': temp}
    elif City.objects.filter(acronym=city):
        list = DailyWeather.objects.filter(city=City.objects.filter(acronym=city).order_by('-day'))
        cityname = list[0].city.name
        temp = list[0].temperature
        date = list[0].day
        data = {'city': cityname,'date':str(date), 'temp': temp}
    else:
        data = {'error': 'this city is not on your DB'}
    return HttpResponse(json.dumps(data), content_type='application/json')


def json_api_temperature_day(request, city, day, month, year):
    if City.objects.filter(name=city):
        date = year+"-"+month+"-"+day
        try:
            data = {'city': city, 
            'date': date,
            'temp': DailyWeather.objects.get(city=City.objects.get(name=city),day=date).temperature,
            }
        except:
            data = {'error': 'We have not the temperature for this day'}
    elif City.objects.filter(acronym=city):
        date = year+"-"+month+"-"+day
        dailyWeather = DailyWeather.objects.get(city=City.objects.filter(acronym=city),day=date)
        try:
            data = {'city': dailyWeather.city.name, 
            'date': date,
            'temp': dailyWeather.temperature,
            }
        except:
            data = {'error': 'We have not the temperature for this day'}
    else:
        data = {'error': 'this city is not on your DB'}
    return HttpResponse(json.dumps(data), content_type='application/json')

