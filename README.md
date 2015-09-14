weatherapi
======

# Instalar el servidor en el entorno de desarrollo (Linux):

## Preparar entorno(linux)

$ apt-get update && apt-get upgrade

$ apt-get install build-essential && python2.7-dev python-setuptools

$ apt-get install postgresql python-psycopg2 libpq-dev

$ easy_install pip

$ pip install virtualenv


## Recuperar proyecto del repositorio y crear virtualenv

$ mkdir -p  ~/myWeatherAPI/ && cd ~/myWeatherAPI/

$ virtualenv venv_weatherapi

$ mkdir source && cd source

$ git clone https://github.com/MTL1991/weatherapi

## Crear DB

$ createdb testweatherdb

## Crear alias cómodo:

echo 'alias dvenv="cd ~/myWeatherAPI/venv_weatherapi/ && source bin/activate && cd ~/myWeatherAPI/source/weatherapi/weathersite"' >> ~/.bash_aliases && source ~/.bash_aliases

## Instalar dependencias del proyecto

$ dvenv

(venv_weatherapi)$ pip install -r ~/myWeatherAPI/source/weatherapi/requirements.txt

## Migrar DB y cargar fixtures en la DB

(venv_weatherapi)$ cd ~/myWeatherAPI/source/weatherapi/weathersite

(venv_weatherapi)$ python manage.py migrate

(venv_weatherapi)$ python manage.py loaddata fixtures/some_data.json

## Lanzar servidor de desarrollo:

(venv_weatherapi)$ python manage.py runserver


# Ejecutar script

## Obteniendo los datos de la web

Bastará con hacer:

$ cd ~/myWeatherAPI/source/weatherapi/script

$ python weather.py -h

De esta forma se lanzará la explicación de uso siguiente:

usage: weather.py [-h] [-c CITY] [-d DAY]

optional arguments:
  -h, --help            show this help message and exit
  -c CITY, --city CITY  Seleccionar ciudad
  -d DAY, --day DAY     Dia concreto en formato dd/mm/yyyy

Nota: Por defecto esta configurado para tomar los datos de la aplicación desplegada en heroku en la dirección http://testmanuel.herokuapp.com/ para utilizar el script con el servidor lanzado en local bastará con modificar en el script la variable serverUrl por aquella que corresponda



