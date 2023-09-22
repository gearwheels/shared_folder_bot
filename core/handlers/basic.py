from aiogram import Bot, types, filters

async def get_start(message: types.Message, command: filters.CommandObject, bot: Bot):
    if message.chat.type != 'private':
        await message.answer(f'Данный бот может использоваться только в личном чате.')
        return
    await message.answer(f'Hello world!')

