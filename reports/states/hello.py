from reports.states.base import BaseState
from reports.tg_buttons import RiverStateButtons
from telebot import types
from reports.states.post import PostState


from reports.models import River




class HelloState(BaseState):
    text = "Виберіть Річку"

    def __init__(self, chat_id=None):
        super().__init__(chat_id)
        self.user = self.get_user()
        self.keyboard.add(RiverStateButtons.pryt_button)
        self.keyboard.add(RiverStateButtons.siret_button)
        self.keyboard.add(RiverStateButtons.cheremosh_button)
        self.keyboard.add(RiverStateButtons.biluy_cheremosh_button)
        self.keyboard.add(RiverStateButtons.chornuy_cheremosh_button)
        self.list_river = [i for i in River.objects.order_by('name_river')]
        print(self.list_river)




    def proccess(self, message: types.Message):
        if hasattr(message, 'data'):
            for river in self.list_river:
                if message.data == f'nextstate:{river}State':
                    self.user.first_name = message.from_user.first_name
                    self.user.last_name = message.from_user.last_name
                    self.user.settings["river"] = river
                    self.user.last_message = ""
                    self.user.save()
                    return PostState(self.chat_id)
        return self


