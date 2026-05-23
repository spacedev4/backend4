import asyncio
from aiogram.client.default import DefaultBotProperties

from aiogram import Bot, Dispatcher
from aiogram.client.session.middlewares.request_logging import logger
from loader import db
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message

def setup_handlers(dispatcher: Dispatcher) -> None:
    """HANDLERS"""
    from handlers import setup_routers

    dispatcher.include_router(setup_routers())


def setup_middlewares(dispatcher: Dispatcher, bot: Bot) -> None:
    """MIDDLEWARE"""
    from middlewares.throttling import ThrottlingMiddleware

    # Spamdan himoya qilish uchun klassik ichki o'rta dastur. So'rovlar orasidagi asosiy vaqtlar 0,5 soniya
    dispatcher.message.middleware(ThrottlingMiddleware(slow_mode_delay=0.5))


def setup_filters(dispatcher: Dispatcher) -> None:
    """FILTERS"""
    from filters import ChatPrivateFilter

    # Chat turini aniqlash uchun klassik umumiy filtr
    # Filtrni handlers/users/__init__ -dagi har bir routerga alohida o'rnatish mumkin
    dispatcher.message.filter(ChatPrivateFilter(chat_type=["private"]))


async def setup_aiogram(dispatcher: Dispatcher, bot: Bot) -> None:
    logger.info("Configuring aiogram")
    setup_handlers(dispatcher=dispatcher)
    setup_middlewares(dispatcher=dispatcher, bot=bot)
    setup_filters(dispatcher=dispatcher)
    logger.info("Configured aiogram")


async def database_connected():
    # Ma'lumotlar bazasini yaratamiz:
    await db.create()
    # await db.drop_users()
    await db.create_table_users()


async def aiogram_on_startup_polling(dispatcher: Dispatcher, bot: Bot) -> None:
    from utils.set_bot_commands import set_default_commands
    from utils.notify_admins import on_startup_notify

    logger.info("Database connected")
    await database_connected()

    logger.info("Starting polling")
    await bot.delete_webhook(drop_pending_updates=True)
    await setup_aiogram(bot=bot, dispatcher=dispatcher)
    await on_startup_notify(bot=bot)
    await set_default_commands(bot=bot)


async def aiogram_on_shutdown_polling(dispatcher: Dispatcher, bot: Bot):
    logger.info("Stopping polling")
    await bot.session.close()
    await dispatcher.storage.close()


def main():
    """CONFIG"""
    from data.config import BOT_TOKEN
    from aiogram.enums import ParseMode
    from aiogram.fsm.storage.memory import MemoryStorage

    bot = Bot(
        token=BOT_TOKEN,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML)
    )
    storage = MemoryStorage()
    dispatcher = Dispatcher(storage=storage)

    dispatcher.startup.register(aiogram_on_startup_polling)
    dispatcher.shutdown.register(aiogram_on_shutdown_polling)
    asyncio.run(dispatcher.start_polling(bot, close_bot_session=True))
    # allowed_updates=['message', 'chat_member']



from googletrans import Translator
dp = Dispatcher()
tarjimon = Translator()


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


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        logger.info("Bot stopped!")
