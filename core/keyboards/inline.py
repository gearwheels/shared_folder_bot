from pathlib import Path

from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardButton 

from core.utils.callbackdata.callbackdata import FolderInfo, FileInfo, CancelInfo
from core.utils.callbackdata.my_callback import dataForCallback
from core.utils.data.globals_var import dict_clients_callbacks
from core.utils.data.paths import dir_for_search


def get_keyboard_folder(paths: list, user_id: str):
    
    keyboard_builder = InlineKeyboardBuilder()
    global dict_clients_callbacks
    dict_clients_callbacks[user_id] = dataForCallback()
    len_dir_for_search = len(dir_for_search)

    for num_key, path in enumerate(paths):
        name_dir = path.split("/")[-1]
        keyboard_builder.button(text=path[len_dir_for_search :], callback_data=FolderInfo(num_key=str(num_key)))
        dict_clients_callbacks[user_id].set_key_and_data(str(num_key), [path, name_dir])

    keyboard_builder.button(
            text="Отмена",
            callback_data=CancelInfo(data="cancel")
    )
    keyboard_builder.adjust(1)

    return keyboard_builder.as_markup()


def get_keyboard_file(paths: list, root_folder: str, user_id: str):
    
    keyboard_builder = InlineKeyboardBuilder()
    global dict_clients_callbacks
    dict_clients_callbacks[user_id] = dataForCallback()
    len_root_folder = len(root_folder)
   
    for num_key, path in enumerate(paths):
        keyboard_builder.button(text=path[len_root_folder :], callback_data=FileInfo(num_key=str(num_key)))
        dict_clients_callbacks[user_id].set_key_and_data(str(num_key), [root_folder, path])

    num_key = len(dict_clients_callbacks[user_id].key_and_data)
    keyboard_builder.button(
            text="Скачать все",
            callback_data=FileInfo(num_key=str(num_key))
    )
    dict_clients_callbacks[user_id].set_key_and_data(str(num_key), [root_folder, "download_all"])

    keyboard_builder.button(
            text="Отмена",
            callback_data=CancelInfo(data="cancel")
    )
    keyboard_builder.adjust(1)

    return keyboard_builder.as_markup()



