from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

bot = Bot(token='2108070415:AAFotrZe9GbEhLUqbE1X0ig8HuzkQNtEdEM')
dp = Dispatcher(bot)

@dp.message_handler()

async def echo_send(message = types.Message):
    #await message.answer(message.text)
    #await message.reply(message.text)
    await bot.send_message(message.from_user.id, message.text)




executor.start_polling(dp, skip_updates=True)


