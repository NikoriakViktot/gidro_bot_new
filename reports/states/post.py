from telebot import types

from reports.states.base import BaseState
from reports.tg_buttons import RiverStateButtons,PostStateButtons
from reports.config import bot
from reports.states.cher import PostCher

class PostState(BaseState):
    text = "Вибиріть ГідроПост"

    def __init__(self, chat_id=None):
        super().__init__(chat_id)
        self.keyboard.add(PostStateButtons.cher_button)


    def proccess(self, message: types.Message):
        print(message)
        if hasattr(message, 'data'):
            if message.data == 'nextstate:PostCher':
                return PostCher(self.chat_id)
        return self
