from telebot import types



class RiverStateButtons:
    river_button = types.InlineKeyboardButton(text='Річки', callback_data='nextstate:RiverState')
    pryt_button = types.InlineKeyboardButton(text='Прут', callback_data='nextstate:prutState')
    siret_button = types.InlineKeyboardButton(text='Сірет', callback_data='nextstate:siretState')
    cheremosh_button = types.InlineKeyboardButton(text='Черемош', callback_data='nextstate:cheremoshState')
    biluy_cheremosh_button = types.InlineKeyboardButton(text='Білий Черемош', callback_data='nextstate:biluy_cheremoshState')
    chornuy_cheremosh_button = types.InlineKeyboardButton(text='Чорний Черемош', callback_data='nextstate:chornuy_cheremoshState')



class PostStateButtons:
    post_button = types.InlineKeyboardButton(text='ГідроПост', callback_data='nextstate:PostState')
    cher_button = types.InlineKeyboardButton(text='ГідроПост Чернівці', callback_data='nextstate:PostCher')


class PostDataButtons:
    last_report_button = types.InlineKeyboardButton(text="Рівень", callback_data='nextstate:Level')
    pagodas_button = types.InlineKeyboardButton(text="Погода", callback_data='nextstate:Pogoda')