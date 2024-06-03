from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def get_keyboard_1():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    button_1 = KeyboardButton('Отправь фото погонов ')
    button_4 = KeyboardButton('Перейти на следующую клавиатуру')
    keyboard.add(button_1, button_4)
    return keyboard

def get_keyboard_2():
    keyboard_2= ReplyKeyboardMarkup(resize_keyboard=True)
    button_3 = KeyboardButton('Отправь фото танка Т-14')
    button_6 = KeyboardButton('Вернуться на 1 клавиатуру')
    keyboard_2.add(button_3, button_6)
    return keyboard_2