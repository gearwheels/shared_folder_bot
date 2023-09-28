from aiogram import Bot, types, filters

from core.server import get_foldernames
from core.keyboards.inline import get_keyboard_folder
from core.utils.data.text import HELP_TEXT, WARNING_PRIVATE_MODE, WARNING_NO_ARG, ANSWER_FOLDER_IS_FOUND

async def get_start(message: types.Message, command: filters.CommandObject, bot: Bot):
    if message.chat.type != 'private':
        await message.answer(WARNING_PRIVATE_MODE)
        return
    await message.answer(f'Чтобы найти нужную папку импользуйте команду /find_folder')


async def find_folder(message: types.Message, command: filters.CommandObject, bot: Bot):
    if message.chat.type != 'private':
        await message.answer(WARNING_PRIVATE_MODE)
        return
    if command.args:
        list_folders = get_foldernames(command.args)
        markup_folders = get_keyboard_folder(list_folders, str(message.from_user.id))
        await message.answer(ANSWER_FOLDER_IS_FOUND.format(command.args), reply_markup=markup_folders)
    else:
        await message.answer(WARNING_NO_ARG)


async def get_help(message: types.Message, command: filters.CommandObject, bot: Bot):
    if message.chat.type != 'private':
        await message.answer(WARNING_PRIVATE_MODE)
        return
    await message.answer(HELP_TEXT)

