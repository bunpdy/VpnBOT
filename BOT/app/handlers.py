from aiogram.filters import CommandStart
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from datetime import datetime

from aiogram import Router
from db import add_user, get_user_balance, conn  # Импортируем из нашего файла db.py

import app.keyboards as kb

router = Router()

class Reg(StatesGroup):
    waiting_for_login = State()  
    waiting_for_password = State()

@router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    """
    Этот обработчик реагирует на команду /start
    """
    # Получаем информацию о пользователе
    user_id = message.from_user.id
    full_name = message.from_user.full_name
    username = message.from_user.username
    reg_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Добавляем пользователя в базу данных
    add_user(conn, user_id, full_name, username, reg_date)
    
    await message.answer(f"Привет, {message.from_user.full_name}! Ты успешно зарегистрирован.", reply_markup=kb.main)

@router.message(Command("register"))
async def register_user(message: Message) -> None:
    await message.answer

@router.message(Command("profile"))
async def show_balance(message: Message) -> None:
    """Показывает профиль пользователя"""
    user_id = message.from_user.id
    balance = get_user_balance(conn, user_id)
    await message.answer(f"💰 Ваш баланс: {balance}\nID:{user_id}\nПодписка активна до n числа")
