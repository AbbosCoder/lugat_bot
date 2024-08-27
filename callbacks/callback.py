from aiogram import types
from aiogram.types import ParseMode
from aiogram.dispatcher import Dispatcher
from config.config import ADMINS
from states.state import SendADS,SendMsg
from aiogram.dispatcher import FSMContext
from keyboards.tugma import kb
from main import cursor,bot
from pytz import timezone
import datetime
def users_count():
    # Execute a query to get the total number of users
    cursor.execute('SELECT COUNT(*) FROM users')
    # Fetch the result of the query
    total_users_count = cursor.fetchone()[0]
    return total_users_count
    
async def on_startup(dp: Dispatcher):
    @dp.callback_query_handler(text='stat',chat_id = ADMINS)
    async def stat(query: types.CallbackQuery):
        uz_tz = timezone('Asia/Tashkent')
        datas = datetime.datetime.now(uz_tz)
        yil_oy_kun = (datetime.datetime.date(datetime.datetime.now()))
        soat_minut_sekund = f"{datas.hour}:{datas.minute}:{datas.second}"
        await query.message.edit_text(f"<b>Umumiy foydalanuvchilar: {users_count()} ta</b>\n"
                                      f"<b>Vaqt: {soat_minut_sekund} | Sana: {yil_oy_kun}</b>",parse_mode='Html',reply_markup=kb.exit_adminpanel())
        await query.answer()
    @dp.callback_query_handler(text='send_msg',chat_id = ADMINS)
    async def send_msg(query: types.CallbackQuery):
        await query.message.edit_text("Yubormoqchi bo'lgan xabaringizni kiriting:\n<i>parse_mode='Html'</i>",parse_mode='Html')
        await query.answer()
        await SendMsg.xabar.set()

    @dp.message_handler(state=SendMsg.xabar,content_types=types.ContentTypes.ANY)
    async def process_location(message: types.Message, state: FSMContext):
    
        # Foydalanuvchilarning id va ismini olish
        cursor.execute('SELECT id, first_name FROM users')
        users = cursor.fetchall()
        await message.answer('Xabar yuborish boshlandi...\n<b>Biroz kuting...</b>',parse_mode='html')
        a,b=0,0
        for user_id, first_name in users:
            # Har bir foydalanuvchiga xabar yuborish
            try:
                await bot.copy_message(chat_id=user_id,
                                       from_chat_id=message.from_user.id,
                                       message_id=message.message_id,
                                       caption=message.caption,
                                       parse_mode=ParseMode.MARKDOWN,
                                       reply_markup=message.reply_markup)
                a+=1
            except Exception as e:
                print(f"Xabar yuborishda xato yuz berdi: {e}")
                b+=1

        await message.answer(f"✅ Reklama muvaffaqiyatli yuborildi!\n<b>Aktiv foydalanuvchilar: {a}\nBotni blocklaganlar: {b}\nYuborilgan xabarlar: {a+b}</b>" ,parse_mode='Html')
        await message.answer( '<b>ADMIN PANEL:</b>',
                             parse_mode=ParseMode.HTML,
                             reply_markup=kb.admin())       
        await state.finish() 
    @dp.callback_query_handler(text='orqaga',chat_id = ADMINS)
    async def orqaga(query: types.CallbackQuery):
        await query.message.edit_text("<b>ADMIN PANEL:</b>",parse_mode='Html', reply_markup=kb.admin())
        await query.answer()        
    @dp.callback_query_handler(text='send_ads',chat_id = ADMINS)
    async def send_ads(query: types.CallbackQuery):
        await query.message.edit_text("Reklama yuboring... ",parse_mode='Html')
        await query.answer()  
        await SendADS.ads.set()

    @dp.message_handler(state=SendADS.ads,content_types=types.ContentTypes.ANY)
    async def add_user_finish(message: types.Message, state: FSMContext):
        cursor.execute('SELECT id, first_name FROM users')
        users = cursor.fetchall()
        await message.answer('Xabar yuborish boshlandi...\n<b>Biroz kuting...</b>',parse_mode='html')
        a,b=0,0
        for user_id, first_name in users:
            # Har bir foydalanuvchiga xabar yuborish
            try:
                await bot.copy_message(chat_id=user_id,
                                       from_chat_id=message.from_user.id,
                                       message_id=message.message_id,
                                       caption=message.caption,
                                       parse_mode=ParseMode.MARKDOWN,
                                       reply_markup=message.reply_markup)
                a+=1
            except Exception as e:
                print(f"Xabar yuborishda xato yuz berdi: {e}")
                b+=1
 
        await message.answer(f"✅ Reklama muvaffaqiyatli yuborildi!\n<b>Aktiv foydalanuvchilar: {a}\nBotni blocklaganlar: {b}\nYuborilgan xabarlar: {a+b}</b>",parse_mode='html' )
        await message.answer( '<b>ADMIN PANEL:</b>',
                             parse_mode=ParseMode.HTML,
                             reply_markup=kb.admin())
        await state.finish()      
   