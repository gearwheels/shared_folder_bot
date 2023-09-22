import asyncio

from aiogram import Bot, Dispatcher, types
import logging
from aiogram.filters import Command
from aiogram import filters


from core.settings import settings
from core.utils.commands import set_commands
from core.handlers.basic import get_start


async def start_bot(bot: Bot):
    await set_commands(bot)
    await bot.send_message(settings.bots.admin_id, text='Бот запущен.')

async def end_bot(bot: Bot):
    await bot.send_message(settings.bots.admin_id, text='Бот отключен.')



async def start():

    logging.basicConfig(level=logging.INFO, 
                        format="%(asctime)s - [%(levelname)s] - %(name)s"
                            "(%(filename)s).%(funcName)s(%(lineno)d) - %(message)s"
                        )
    bot = Bot(token=settings.bots.bot_token, parse_mode='HTML')
    
    dp = Dispatcher()
    dp.startup.register(start_bot)
    dp.shutdown.register(end_bot)


    dp.message.register(get_start, filters.CommandStart())

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(start())


