
import requests


import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "gidro_bot.settings")

import django
django.setup()

from django.core.management import call_command
from reports.models import River

list_river = [i for i in River.objects.order_by('name_river')]
print(list_river)

API_KEY = os.getenv('APIKEY')

CITY ='Чернівці'

DATA = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&units=metric&APPID={API_KEY}")
print(DATA.json().get( "weather"))
print(  f"Температура: {DATA.json().get('main')['temp']}°C",
                         f"Вологість: {DATA.json().get('main')['humidity']}%",
                         f"Швидкість  вітру: {DATA.json().get('wind')['speed']} km/h",)