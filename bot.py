import logging
from aiogram import Bot, Dispatcher, executor, types, md
 
API_TOKEN = '...............................................'
 
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)
 
@dp.message_handler(commands=['start'])
async def start_reg(message: types.Message):
    await message.answer(message.text)
 
@dp.message_handler()
async def echo(message: types.Message):
    await message.answer('Ты мне что-то написал')
 
 
if name == 'main':
    executor.start_polling(dp, skip_updates=True)