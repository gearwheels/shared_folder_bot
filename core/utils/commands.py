from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault, BotCommandScopeAllPrivateChats


async def set_commands(bot: Bot):
    strs_commands = ['start', 'help', ]
    strs_description = ['Начало работы', 'Помощь']
    commands = []
    for num, com in enumerate(strs_commands):
        commands.append(BotCommand(command=com, description=strs_description[num]))

    await bot.set_my_commands(commands, BotCommandScopeAllPrivateChats())