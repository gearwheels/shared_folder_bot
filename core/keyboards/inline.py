from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardButton
from pathlib import Path

from core.utils.callbackdata.callbackdata import FolderInfo, FileInfo, CancelInfo


def get_keyboard_folder(paths: list):
    
    keyboard_builder = InlineKeyboardBuilder()
    name_dir = path.split("/")[-1]

    for path in paths:
        keyboard_builder.button(text=path, callback_data=FolderInfo(path=path, data=name_dir))

    keyboard_builder.button(
            text="Отмена",
            callback_data=CancelInfo(data="cancel")
    )
    keyboard_builder.adjust(1)

    return keyboard_builder.as_markup()


def get_keyboard_file(paths: list, root_folder: str):
    
    keyboard_builder = InlineKeyboardBuilder()
   
    for path in paths:
        keyboard_builder.button(text=path, callback_data=FileInfo(path=root_folder, data=path))

    keyboard_builder.button(
            text="Скачать все",
            callback_data=FileInfo(path=root_folder, data="download_all")
    )
    keyboard_builder.button(
            text="Отмена",
            callback_data=CancelInfo(data="cancel")
    )
    keyboard_builder.adjust(1)

    return keyboard_builder.as_markup()



# def get_confirm_Ikeyboard(names_btn=['confirm', 'cancel']): 
#     CURRENT_LVL = 4
#     keyboard_builder = InlineKeyboardBuilder()
#     check_confirm = lambda n_btn: n_btn == 'confirm'
#     for name_btn in names_btn:
#         keyboard_builder.button(text=name_btn, callback_data=ConfirmInfo(lvl=CURRENT_LVL, flag=check_confirm(name_btn)))
#     keyboard_builder.button(
#             text="backstep",
#             callback_data=BackstepInfo(lvl=CURRENT_LVL - 1)
#     )
#     keyboard_builder.adjust(1)
#     return keyboard_builder.as_markup()


