from aiogram import Bot
from aiogram.types import CallbackQuery, FSInputFile
from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardButton
from aiogram.filters.callback_data import CallbackData
from aiogram.utils.chat_action import ChatActionSender

from core.keyboards.inline import get_keyboard_folder, get_keyboard_file
from core.server import get_all_filenames 
from core.utils.data.globals_var import dict_clients_callbacks
from core.utils.data.text import ANSWER_OPEN_FOLDER, SHUTDOWN_INLINE, CANCEL_MSG
from core.utils.callbackdata.callbackdata import FolderInfo, FileInfo, CancelInfo
from core.server import creat_archive, del_archive
from core.utils.data.globals_var import dict_clients_callbacks

async def find_file(call: CallbackQuery, bot: Bot, callback_data: FolderInfo):
    client_id = str(call.from_user.id)
    key_id = callback_data.num_key 

    data_list = dict_clients_callbacks[client_id].get_data(key_id)

    path_folder = data_list[0]
    foldername = data_list[1]
    list_files = []

    answer = ANSWER_OPEN_FOLDER.format(foldername)
    
    list_files = get_all_filenames(path_folder)
    files_markup = get_keyboard_file(list_files, root_folder=path_folder, user_id=client_id)
    
    await call.message.edit_text(SHUTDOWN_INLINE.format(foldername))
    await call.message.answer(answer, reply_markup=files_markup)
    await call.answer()

async def upload_file(call: CallbackQuery, bot: Bot, callback_data: FileInfo):
    client_id = str(call.from_user.id)
    key_id = callback_data.num_key 

    data_list = dict_clients_callbacks[client_id].get_data(key_id)

    root_folder = data_list[0]
    filename = data_list[1]

    # document = FSInputFile()

    if filename == "download_all":
        await call.message.edit_text(SHUTDOWN_INLINE.format(root_folder.split('/')[-1]))
        async with ChatActionSender.upload_document(chat_id=call.message.chat.id, bot=bot):
            archive_folder = creat_archive(root_folder,client_id) # заархивировать все файлы из папки root_folder
            root_folder  # отправить все файлы из папки root_folder
            document = FSInputFile(archive_folder)
            await bot.send_document(call.message.chat.id, document=document)
        await del_archive(root_folder)
    else:
        await call.message.edit_text(SHUTDOWN_INLINE.format(filename.split('/')[-1]))
        async with ChatActionSender.upload_document(chat_id=call.message.chat.id, bot=bot):
            document = FSInputFile(filename)# отправить файл указаный по пути root_folder
            await bot.send_document(call.message.chat.id, document=document)
        

    # list_files = []

    # answer = ANSWER_OPEN_FOLDER.format(foldername)
    
    # list_files = get_all_filenames(path_folder)
    # files_markup = get_Ikeyboard(list_files, folder=False)
    
    await call.message.edit_text(SHUTDOWN_INLINE.format(filename))
    # await call.message.answer(answer)
    await call.answer()

async def cancel(call: CallbackQuery, bot: Bot, callback_data: FileInfo):
    
    await call.message.edit_text(CANCEL_MSG)
    await call.answer()








