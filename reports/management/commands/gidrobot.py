from django.core.management.base import BaseCommand
from reports.config import bot
from reports.states.hello import HelloState

user_states = {}

@bot.message_handler(commands=['Start'])
def begin_conversation(message):
    s = HelloState(message.chat.id)
    s.display()
    user_states[message.chat.id] = s
    print(message)




@bot.callback_query_handler(func=lambda data: True)
def callback_handler(message):
    s = user_states[message.from_user.id]
    s2 = s.proccess(message)
    s2.display()
    user_states[message.from_user.id] = s2

    print(message)



# print(user_states)
class Command(BaseCommand):
    help = 'start'


    def handle(self, *args, **options):
        print('ok')

        bot.infinity_polling()