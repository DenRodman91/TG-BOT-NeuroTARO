from aiogram import types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.fsm.context import FSMContext
from .fsm_states import AddUserDetails, Req_GPT
from gpt_integration.gpt import get_chatgpt_response
from database.db import add_user, get_user_data, save_taro_response
import logging
from .main import bot
# Команды бота
commands = {
    'Разложить ТАРО': 'new_taro',
    'Мои расклады': 'my_taro',
    'Мои данные': 'my_data',
    'Подписка': 'payment',
}

# Приветственное сообщение
async def start(id):
    user_exists = await add_user(id)
    buttons = [[InlineKeyboardButton(text=i, callback_data=commands[i])] for i in commands]
    inline_kb = InlineKeyboardMarkup(inline_keyboard=buttons)
    tex = '''Приветствую вас, искатели мудрости! 🌟
    Добро пожаловать в наш Таро-бот!'''
    
    await bot.send_message(chat_id=id, text=tex, reply_markup=inline_kb)

# Обработка команды /add
async def add(message, state):
    user_id = message.from_user.id
    user_data = await get_user_data(user_id)
    if not user_data:
        await message.answer("Введите имя:")
        await state.set_state(AddUserDetails.waiting_for_name)
    else:
        await message.answer("Ваши данные уже заполнены.")