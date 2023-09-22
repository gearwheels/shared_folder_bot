from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardButton

from core.utils.callbackdata import MeetingInfo, SugarInfo, SyrupsInfo, DrinksInfo, BackstepInfo, ConfirmInfo


def get_room_Ikeyboard(rooms: list, cb_data: list):
    CURRENT_LVL = 0
    keyboard_builder = InlineKeyboardBuilder()
    for num, room in enumerate(rooms):
        keyboard_builder.button(text=room, callback_data=MeetingInfo(num_room=room, data_room=cb_data[num], lvl=CURRENT_LVL))
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


