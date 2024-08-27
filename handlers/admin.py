from aiogram import types
from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher.filters import Command
from states.state import PanelStates
from aiogram.dispatcher import FSMContext
from keyboards.tugma import kb
from config.config import ADMINS
from art import *


async def on_startup(dp: Dispatcher):
    tprint("Abbosbek_Turdaliyev")
    @dp.message_handler(commands=['start'], chat_id=ADMINS)
    async def start_command(message: types.Message):
        name = message.from_user.first_name
        await message.answer(f"<i>Assalomu alaykum! <b>{name}</b></i>\n<b>ADMIN PANEL:</b>",parse_mode=types.ParseMode.HTML,reply_markup=kb.admin())
    
    
        

    
    
    