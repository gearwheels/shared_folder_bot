import asyncio

from aiogram import Bot, Dispatcher, types
import logging
from aiogram.filters import Command
from aiogram import filters


from core.settings import settings
from core.utils.commands import set_commands
from core.handlers.basic import get_start, find_folder, get_help
from core.handlers.callbacks import find_file, upload_file, cancel
from core.utils.callbackdata.callbackdata import FolderInfo, FileInfo, CancelInfo


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
    dp.message.register(find_folder, Command(commands='find_folder'))
    dp.message.register(get_help, Command(commands='help'))
    
    dp.callback_query.register(find_file, FolderInfo.filter())
    dp.callback_query.register(upload_file, FileInfo.filter())
    dp.callback_query.register(cancel, CancelInfo.filter())

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(start())


