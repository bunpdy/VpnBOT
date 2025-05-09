from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Получить доступ к серверу")],
    [KeyboardButton(text="Мой профиль"), KeyboardButton(text="О приложении")]
],  resize_keyboard=True,
    input_field_placeholder="Выберите пункт меню")