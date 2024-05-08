from aiogram.types import Message, CallbackQuery
from aiogram import Bot, Dispatcher, executor

from knopkalarfayli import asosiymenubutton, maxsulotlarbutoon

api = '6487583369:AAELjgDAFRTQmIORQq4FXydcK61QAu5CU6g'

bot = Bot(api)
dp = Dispatcher(bot)

@dp.message_handler(commands='start')
async def start(message: Message):
    chatid= message.chat.id
    await bot.send_message(chat_id=chatid, text='Xush kelibsiz', reply_markup=asosiymenubutton())


@dp.message_handler()
async def getcategory(message: Message):
    chatid = message.chat.id
    kategoriya = message.text

    await bot.send_message(chat_id=chatid, text=kategoriya,
                           reply_markup=maxsulotlarbutoon(kategoriya))


executor.start_polling(dp, skip_updates=True)