# -*- encoding: utf-8 -*-
from django.forms import *

from ppal.models import *


class CityForm(ModelForm):
    class Meta:
        model = City
        # The creator of the trab is the current site visitor.
        
    def __init__(self, *args, **kwargs):
        super(CityForm, self).__init__(*args, **kwargs)
        self.fields['name'].label = "Name"
        self.fields['acronym'].label = "Acronym"

class WeatherForm(ModelForm):
    class Meta:
        model = DailyWeather
        exclude = ['city']
        # The creator of the trab is the current site visitor.
        
    def __init__(self, *args, **kwargs):
        super(WeatherForm, self).__init__(*args, **kwargs)
        self.fields['day'].label = "Date"
        self.fields['temperature'].label = "Temperature"

class UserForm(ModelForm):
    password = CharField(label ="Password" ,widget=PasswordInput())
    password2 = CharField(label ="Repeat Password",widget=PasswordInput())


    class Meta:
        model = User
        fields = ('username', 'email')


    def clean_password2(self):
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')

        if password and password2 and password != password2:
            raise ValidationError('Passwords do not match')

        return password2

    def save(self, commit=True):
        user = super(UserForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user
