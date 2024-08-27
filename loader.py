from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from config.config import TOKEN
# Botni yaratamiz
bot = Bot(token=TOKEN)
# Dispatcher yaratamiz
storage = MemoryStorage()

dp = Dispatcher(bot, storage=storage)