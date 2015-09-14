from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.core.urlresolvers import reverse
from ppal.models import *



# Register your models here.

class CityAdmin(admin.ModelAdmin):
    list_display = ('name','acronym')

class DailyWeatherAdmin(admin.ModelAdmin):
    list_display = ('city','day','temperature')

admin.site.register(City, CityAdmin)
admin.site.register(DailyWeather, DailyWeatherAdmin)
