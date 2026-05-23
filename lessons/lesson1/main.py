import asyncio
from googletrans import Translator


from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message

TOKEN = "8627476748:AAEcx5yCK3frZiuQHFoWjtbRMN88OohJTxE"


dp = Dispatcher()
tarjimon = Translator()

# Command handler

# /start ga javob berish

@dp.message(Command("start"))
async def command_start_handler(message: Message) -> None:
    await message.answer("bu bot aiogram yordamida qilingan")

# /help ga javob berish

@dp.message(Command("help"))
async def command_start_handler(message: Message) -> None:
    await message.reply("bu bot test uchun yasalgan")

# /tarjima ga yozilgan textni tarjima qilib berish

@dp.message(Command("tarjima"))
async def command_start_handler(message: Message) -> None:
    result = await tarjimon.translate(message.text, src='uz', dest='en')
    await message.answer(result.text)

# /dollar ga dollar kursini chiqarib berish
# oldingi darsga karab yasalgan

import requests

API_KEY = "81a4209567701ec760bfbf6e"

@dp.message(Command("dollar"))
async def command_start_handler(message: Message) -> None:

    currency = 'USD'
    url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/pair/{currency}/UZS"
    responce = requests.get(url)
    kurs = responce.json()['conversion_rate']
    await message.answer(f"dollar kursi {kurs} UZS")

# /havo ga havo haqida malumot chiqarib berish

import python_weather # pypi dan topdim

@dp.message(Command('havo'))

async def command_start_handler(message: Message) -> None:
    async with python_weather.Client(unit=python_weather.METRIC) as client:
        weather = await client.get('urgench')
        await message.answer(f"Urgenchda havo {weather.temperature}°")


# Run the bot
async def main() -> None:
    bot = Bot(token=TOKEN)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())