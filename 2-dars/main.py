from aiogram.types import Message, CallbackQuery
from aiogram import Bot, Dispatcher, executor
from keyboards import shaharqoshish, asosiymenyubutton
from database import registrshahar

api = '7093062747:AAGXoOJzWHveqYXSHhIyg5FA8esVj8_ZNAU'
bot= Bot(api)
dp = Dispatcher(bot)

@dp.message_handler(commands='start')
async def start(message: Message):
    chatid= message.chat.id
    await bot.send_message(chat_id=chatid, text='Xush kelibsiz. Shahar nomini kiriting', reply_markup=asosiymenyubutton(chatid))


@dp.message_handler()
async def getshahar(message: Message):
    chatid= message.chat.id
    shahar = message.text
    await bot.send_message(chat_id=chatid, text='Obhavo', reply_markup=shaharqoshish(shahar))


@dp.callback_query_handler(lambda call: 'shahar' in call.data)
async def addshahar(callback: CallbackQuery):
    chatid = callback.message.chat.id
    shahar  = callback.data.split('_')[1]
    registrshahar(name=shahar, chatid=chatid)
    await bot.send_message(chat_id=chatid, text=shahar, reply_markup=asosiymenyubutton(chatid))

executor.start_polling(dp, skip_updates=True)