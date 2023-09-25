from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardButton

from core.utils.callbackdata import MeetingInfo, SugarInfo, SyrupsInfo, DrinksInfo, BackstepInfo, ConfirmInfo


def get_Ikeyboard(paths: list):
    CURRENT_LVL = 0
    keyboard_builder = InlineKeyboardBuilder()
    for path in paths:
        keyboard_builder.button(text=path, callback_data=path)
    keyboard_builder.adjust(1)
    return keyboard_builder.as_markup()

def get_confirm_Ikeyboard(names_btn=['confirm', 'cancel']): 
    CURRENT_LVL = 4
    keyboard_builder = InlineKeyboardBuilder()
    check_confirm = lambda n_btn: n_btn == 'confirm'
    for name_btn in names_btn:
        keyboard_builder.button(text=name_btn, callback_data=ConfirmInfo(lvl=CURRENT_LVL, flag=check_confirm(name_btn)))
    keyboard_builder.button(
            text="backstep",
            callback_data=BackstepInfo(lvl=CURRENT_LVL - 1)
    )
    keyboard_builder.adjust(1)
    return keyboard_builder.as_markup()


