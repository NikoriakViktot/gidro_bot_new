from telebot import types

from reports.states.base import BaseState
from reports.tg_buttons import PostDataButtons


class PostCher(BaseState):
    text = "Вибиріть дані ГідроПоста"

    def __init__(self, chat_id=None):
        super().__init__(chat_id)
        self.user = self.get_user()
        self.keyboard.add(PostDataButtons.last_report_button)
        self.keyboard.add(PostDataButtons.pagodas_button)



def proccess(self, message: types.Message):
    if hasattr(message, 'data'):
        if message.data == 'nextstate:Level':
            from reports.states.level import Level
            return Level(self.chat_id)
        if message.data == 'nextstate:Pogoda':
            from reports.states.pogoda import Pogoda
            return Pogoda(self.chat_id)
    return self
