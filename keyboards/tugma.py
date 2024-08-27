from aiogram import types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup,KeyboardButton,ReplyKeyboardMarkup


class Keyboards:

    def admin(self):
        inbn = InlineKeyboardMarkup(row_width=2)
        bn1 = InlineKeyboardButton("👥 Statika 📊",callback_data='stat')
        bn2 = InlineKeyboardButton("📣 Reklama yuborish 🔔",callback_data='send_ads')
        bn3 = InlineKeyboardButton("✉️ Xabar yuborish", callback_data='send_msg')
        inbn.add(bn1,bn2,bn3)
        return inbn
    def exit_adminpanel(self):
        orqaga = InlineKeyboardMarkup()
        back = InlineKeyboardButton("🔙 orqaga",callback_data='orqaga')
        orqaga.add(back)
        return orqaga
    def social_media(self):
        social = InlineKeyboardMarkup(row_width=3)
        insta = InlineKeyboardButton('Instagram',url='instagram.com/@abbosbek_turdaliyev')
        channel = InlineKeyboardButton('Loading...', url='t.me/LOADING_my_point')
        
        social.add(insta,channel)  
kb = Keyboards()    
