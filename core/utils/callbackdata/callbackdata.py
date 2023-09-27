from aiogram.filters.callback_data import CallbackData


class FolderInfo(CallbackData, prefix='dir'):
    path: str # путь к папке/файлу
    data: str # название кнопки  
    
class FileInfo(FolderInfo, prefix='file'):
    pass 

class CancelInfo(CallbackData, prefix='cancel'):
    data: str # название кнопки  
