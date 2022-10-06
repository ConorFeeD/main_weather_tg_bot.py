from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


CITY = InlineKeyboardMarkup(row_width=1).add(InlineKeyboardButton(text='Ввести название города', callback_data="city"))
TODAY = InlineKeyboardMarkup(row_width=1).add(InlineKeyboardButton(text='Узнать погоду где-то ещё?', callback_data="today"))
