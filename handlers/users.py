from aiogram import types
# from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup
from aiogram.dispatcher import Dispatcher
from keyboards.tugma import kb
from main import cursor,conn,bot
from .lugat import get_definition
from uz_en_dictionary import Translator

uz = Translator(from_lang='en', to='uz')
en = Translator(from_lang='uz', to='en')

def user_db(user_id,first_name,username):
       # Foydalanuvchi ma'lumotlarini tekshiramiz
    cursor.execute('SELECT * FROM users WHERE id = ?', (user_id,))
    existing_user = cursor.fetchone()
    print(existing_user)
    if not existing_user:
        # Foydalanuvchi mavjud emas, ma'lumotlar bazasiga qo'shamiz
        cursor.execute('''
            INSERT INTO users (id, first_name, username)
            VALUES (?, ?, ?)
        ''', (user_id, first_name, username))
        conn.commit() 

async def on_startup(dp: Dispatcher):
    @dp.message_handler(commands=['start'])
    async def start_command(message: types.Message):
        user_id = message.from_user.id
        first_name = message.from_user.first_name
        username = message.from_user.username
        user_db(user_id,first_name,username)
        await message.answer("Assalomu alaykum! Botga xush kelibsiz!")
    @dp.message_handler(commands=['yordam'])
    async def help(message: types.Message):
        await message.answer("admin: @Abbosbek_Turdaliyev")
    @dp.message_handler(content_types='text')
    async def help(message: types.Message):
        info = get_definition(message.text)
        tarjima = uz.translate(message.text)
        try:
            definition = info[0]
            sinonim = info[1]
            messageInfo = ''
            for i in definition:
                messageInfo +=f'🔹 {i}\n'
            messageSinonim = '<b>SYNONYMS:</b>\n'
            for i in sinonim:
                messageSinonim+=f'   ♦️ <code>{i}</code>\n'
              
            try:
                messageANTONYMS = '<b>ANTONYMS:</b>\n'  
                ANTONYMS = info[2]
                if ANTONYMS == []:
                    messageANTONYMS = ''
                for i in ANTONYMS:
                    messageANTONYMS +=f'   ◾️ <code>{i}</code>\n'
            except:
                pass

            await message.answer(f'Tarjima UZ: <strong>{tarjima}.</strong>\n\n{messageInfo} \n {messageSinonim} \n {messageANTONYMS}',parse_mode='html')
        except:
            
            error = f"Word {message.text} doesn't exist in dictionary" 
            await message.answer(error)    
            await message.answer(en.translate(message.text))