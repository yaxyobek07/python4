import sqlite3

from aiogram.types import Message, CallbackQuery
from aiogram import Bot, Dispatcher, executor

from knopkalar import asosiymenubutton, maxsulotlarbutoon,  orqagabutton

api = '7093062747:AAFXI1iVFKD8OPCe4iu8F07WRFB-7tWxElI'

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


@dp.callback_query_handler(lambda call: "foods" in call.data)
async def getitem(callback: CallbackQuery):
    chatid = callback.message.chat.id
    food_id = callback.data.split('_')[1]
    database = sqlite3.connect('magazin.sqlite')
    cursor = database.cursor()

    cursor.execute('''SELECT name, price, about, image, category FROM foods WHERE id = ?''',
                   (food_id, ))
    item = cursor.fetchone()
    name = item[0]
    price = item[1]
    about = item[2]
    image = item[3]
    categry = item[4]
    text = f'Maxsulot nomi: {name}\nNarxi: {price}\n\n{about}'
    await bot.delete_message(chat_id=chatid, message_id=callback.message.message_id)
    await bot.send_photo(chat_id=chatid, caption=text, photo=image, reply_markup=orqagabutton(categry))



@dp.callback_query_handler(lambda call: "orqaga" in call.data)
async def getitem(callback: CallbackQuery):
    chatid = callback.message.chat.id
    category = callback.data.split('_')[1]

    await bot.delete_message(chat_id=chatid, message_id=callback.message.message_id)
    await bot.send_message(chat_id=chatid, text=category, reply_markup=maxsulotlarbutoon(category))

executor.start_polling(dp, skip_updates=True)