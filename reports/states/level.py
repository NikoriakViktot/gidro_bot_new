from telebot import types
from reports.models import GidroPost, PostReport
from reports.states.base import BaseState

riv = PostReport.objects.all()

# if self.last_report:
#     self.last_report.water_level
# level_post = riv.get(water_level=1)
# print(level_post)
class Level(BaseState):
    text = ""

    def __init__(self, chat_id=None):
        super().__init__(chat_id)
        self.user = self.get_user()
        # bot.send_message(self.chat_id,
        #
        #                  reply_markup=self.keyboard)

    def proccess(self, message: types.Message):
        if hasattr(message, 'data'):
            if message.data == 'nextstate:HelloState':
                return GidroPost(self.chat_id)
        return self







