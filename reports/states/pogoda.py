import os
import requests
from telebot import types
from reports.config import bot
from reports.models import GidroPost
from reports.states.base import BaseState

API_KEY = os.getenv('APIKEY')
Q_Set = GidroPost.objects.all()
CITY = Q_Set.get(post='Чернівці')

DATA = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&units=metric&APPID={API_KEY}")


class Pogoda(BaseState):
    text = ""

    def __init__(self, chat_id=None):
        super().__init__(chat_id)
        self.user = self.get_user()

    def pog(self):
        bot.send_message(self.chat_id,
                         f"Температура: {DATA.json().get('main')['temp']}°C",
                         f"Вологість: {DATA.json().get('main')['humidity']}%",
                         f"Швидкість  вітру: {DATA.json().get('wind')['speed']} km/h",
                         reply_markup=self.keyboard)



    def proccess(self, message: types.Message):
        if hasattr(message, 'data'):
            if message.data == 'nextstate:HelloState':
                return GidroPost(self.chat_id)
        return self







