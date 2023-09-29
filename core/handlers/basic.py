from aiogram import Bot, types, filters
from aiogram.enums import ContentType

from core.server import get_foldernames
from core.keyboards.inline import get_keyboard_folder
from core.utils.data.text import HELP_TEXT, WARNING_PRIVATE_MODE, WARNING_NO_ARG, ANSWER_FOLDER_IS_FOUND, ANSWER_NOT_FOUND_FOLDER
from core.utils.data.globals_var import dp
from core.utils.data.paths import id_client_json
from core.utils.json_r_w import JsonRW


id_client = JsonRW(id_client_json)


@dp.message(filters.CommandStart())
async def get_start(message: types.Message, command: filters.CommandObject, bot: Bot):
    list_id_client = id_client.read_json()
    list_id_client = list(list_id_client.keys())
    print("list_id_client ", list_id_client)

    if message.chat.type == 'private':
        if str(message.from_user.id) in list_id_client:
            await message.answer(f'Для поиска директории на сервере введите часть имени директории.')
        else: 
            await message.answer("Отказано в доступе, обратитесь в поддержку для того, чтобы получить доступ к боту.")
    else:
        await message.answer(WARNING_PRIVATE_MODE)

@dp.message(filters.Command(commands='help'))
async def get_help(message: types.Message, command: filters.CommandObject, bot: Bot):
    list_id_client = id_client.read_json()
    list_id_client = list(list_id_client.keys())
    print("list_id_client ", list_id_client)

    if message.chat.type == 'private':
        if str(message.from_user.id) in list_id_client:
            await message.answer(HELP_TEXT)
        else: 
            await message.answer("Отказано в доступе, обратитесь в поддержку для того, чтобы получить доступ к боту.")
    else:
        await message.answer(WARNING_PRIVATE_MODE)

@dp.message() # filters=ContentType.TEXT
async def find_folder(message: types.Message, bot: Bot):
    list_id_client = id_client.read_json()
    list_id_client = list(list_id_client.keys())
    print("list_id_client ", list_id_client)

    if message.chat.type == 'private':
        if str(message.from_user.id) in list_id_client:
            if len(message.text)>0:
                list_folders = get_foldernames(message.text)
                if list_folders:
                    markup_folders = get_keyboard_folder(list_folders, str(message.from_user.id))
                    await message.answer(ANSWER_FOLDER_IS_FOUND.format(message.text), reply_markup=markup_folders)
                else:
                    await message.answer(ANSWER_NOT_FOUND_FOLDER, reply_markup=None)
            else:
                await message.answer("Вы отправили пустое сообщение.")
        else:
            await message.answer("Отказано в доступе, обратитесь в поддержку для того, чтобы получить доступ к боту.")
    else:
        await message.answer(WARNING_PRIVATE_MODE)


