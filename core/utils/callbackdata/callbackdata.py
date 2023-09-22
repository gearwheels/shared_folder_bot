from aiogram.filters.callback_data import CallbackData

class MeetingInfo(CallbackData, prefix='meeting'):
    num_room: str # номер переговорки 
    data_room: str # этаж на котором находится переговорка 
    lvl: int # уровень погрудения в меню и подменю 


class DrinksInfo(CallbackData, prefix='dr'):
    data: str # данные о выбранном item-e 
    lvl: int # уровень погрудения в меню и подменю 

class SugarInfo(DrinksInfo, prefix='sug'):
    name_drink: str # название напитка которому выбрали дополнительные параметры (саха, сироп и тд)

class SyrupsInfo(SugarInfo, prefix='syr'):
    pass 

class BackstepInfo(CallbackData, prefix='bs'):
    lvl: int # уровень погрудения в меню и подменю 

class ConfirmInfo(BackstepInfo, prefix='conf'):
    flag: bool # подтверждение заказа / отмена заказа. True/False
    pass 
