import logging
from aiogram.utils.exceptions import NetworkError
from aiogram import  Dispatcher, executor
from config.config import  admin_id
import sqlite3
from loader import *
# Loggingni sozlaymiz
logging.basicConfig(level=logging.INFO)
conn = sqlite3.connect('data/users.db')
cursor = conn.cursor()

# Foydalanuvchilar jadvalini yaratamiz
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        first_name TEXT,
        username TEXT
    )
''')
conn.commit()

# Admin va User kodlarini import qilib olib kelamiz
import handlers.admin as admin
import handlers.users as users
import callbacks.callback as callback
async def on_startup(dp: Dispatcher):
    # Admin va User modullarini ishga tushiramiz
    try:
        await dp.bot.send_message(chat_id=admin_id, text="Bot ishga tushdi! /start ")
    except Exception as e:
        print(e)    
    await admin.on_startup(dp)
    await users.on_startup(dp)
    await callback.on_startup(dp)

if __name__ == '__main__':
    try:
        executor.start_polling(dp,on_startup=on_startup)
    except:
        pass

