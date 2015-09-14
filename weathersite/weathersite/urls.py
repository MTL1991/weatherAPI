from django.conf.urls import patterns, include, url
from django.contrib import admin

from ppal.views import *

urlpatterns = patterns('',
    # Examples:
    # url(r'^blog/', include('blog.urls')),
    url(r'^login/$', user_login, name='user_login'),
    url(r'^logout/$', user_logout, name='user_logout'),
    url(r'^user/create/$', create_user, name='create_user'),
    url(r'^admin/', include(admin.site.urls)),

)
urlpatterns += patterns('',
    url(r'^$', show_city_today, name='show_city'),
    url(r'^city/add/$', create_city, name='create_city'),
    url(r'^weather/(?P<num>\d+)/$', show_daily_temperatures, name='daily_weather'),
    url(r'^weather/(?P<pk>\d+)/add$', create_daily_weather, name='create_daily_weather'),
    url(r'^api/(?P<city>.+)/$', json_api_temperature, name='api'),
    url(r'^api/(?P<city>.+)/(?P<day>\d{1,2})/(?P<month>\d{1,2})/(?P<year>\d{4})$', json_api_temperature_day, name='api_day'),
)
urlpatterns += patterns('',
    url(r'^api/$', api_info, name='api_info'),
    url(r'^api/(?P<city>.+)/$', json_api_temperature, name='api'),
    url(r'^api/(?P<city>.+)/(?P<day>\d{1,2})/(?P<month>\d{1,2})/(?P<year>\d{4})$', json_api_temperature_day, name='api_day'),
)
