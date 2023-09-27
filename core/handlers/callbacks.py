from aiogram import Bot
from aiogram.types import CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardButton
from aiogram.filters.callback_data import CallbackData

from core.keyboards.inline import get_keyboard_folder, get_keyboard_file
from core.server import get_all_filenames
from core.utils.data.text import ANSWER_OPEN_FOLDER, SHUTDOWN_INLINE, CANCEL_MSG
from core.utils.callbackdata.callbackdata import FolderInfo, FileInfo, CancelInfo

async def find_file(call: CallbackQuery, bot: Bot, callback_data: FolderInfo):
    client_id = str(call.from_user.id)

    path_folder = callback_data.path # СДЕЛАТЬ ОТДЕЛЬНЫЙ КЛАСС ДЛЯ CALLBACK для каждой клавы 
    foldername = callback_data.data
    list_files = []

    answer = ANSWER_OPEN_FOLDER.format(foldername)
    
    list_files = get_all_filenames(path_folder)
    files_markup = get_keyboard_file(list_files, root_folder=path_folder)
    
    await call.message.edit_text(SHUTDOWN_INLINE.format(foldername))
    await call.message.answer(answer, reply_markup=files_markup)
    await call.answer()

async def upload_file(call: CallbackQuery, bot: Bot, callback_data: FileInfo):
    client_id = str(call.from_user.id)

    root_folder = callback_data.path 
    filename = callback_data.data

    if filename == "download_all":
        root_folder # заархивировать и отправить все файлы из папки root_folder


    else:
        # отправить файл указаный по пути root_folder

    # list_files = []

    # answer = ANSWER_OPEN_FOLDER.format(foldername)
    
    # list_files = get_all_filenames(path_folder)
    # files_markup = get_Ikeyboard(list_files, folder=False)
    
    await call.message.edit_text(SHUTDOWN_INLINE.format(foldername))
    await call.message.answer(answer)
    await call.answer()

async def cancel(call: CallbackQuery, bot: Bot, callback_data: FileInfo):
    
    await call.message.edit_text(CANCEL_MSG)
    await call.answer()








