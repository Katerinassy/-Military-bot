from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def get_keyboard_1_inline():
    keyboard_inline = InlineKeyboardMarkup(row_width=2)
    but_inline = InlineKeyboardButton('Ознакомиться подробнее', url='https://ru.wikipedia.org/wiki/%D0%92%D0%BE%D0%B8%D0%BD%D1%81%D0%BA%D0%B8%D0%B5_%D0%B7%D0%B2%D0%B0%D0%BD%D0%B8%D1%8F_%D0%B8_%D0%B7%D0%BD%D0%B0%D0%BA%D0%B8_%D1%80%D0%B0%D0%B7%D0%BB%D0%B8%D1%87%D0%B8%D1%8F_%D0%B2_%D0%92%D0%BE%D0%BE%D1%80%D1%83%D0%B6%D1%91%D0%BD%D0%BD%D1%8B%D1%85_%D1%81%D0%B8%D0%BB%D0%B0%D1%85_%D0%A0%D0%BE%D1%81%D1%81%D0%B8%D0%B9%D1%81%D0%BA%D0%BE%D0%B9_%D0%A4%D0%B5%D0%B4%D0%B5%D1%80%D0%B0%D1%86%D0%B8%D0%B8#%D0%A1%D0%BE%D0%BB%D0%B4%D0%B0%D1%82%D1%8B,_%D1%81%D0%B5%D1%80%D0%B6%D0%B0%D0%BD%D1%82%D1%8B,_%D1%81%D1%82%D0%B0%D1%80%D1%88%D0%B8%D0%BD%D1%8B')
    but_inline2 = InlineKeyboardButton('Почитать статью о том, как читать погоны', url='https://tass.ru/armiya-i-opk/17819415?ysclid=lwurzklti7226140666')
    keyboard_inline.add(but_inline, but_inline2)

    return keyboard_inline

def get_keyboard_2_inline():
    keyboard_inline2 = InlineKeyboardMarkup(row_width= 2)
    but_inline3 = InlineKeyboardButton('Посмотреть другие модели', url='https://ru.wikipedia.org/wiki/%D0%A1%D0%BF%D0%B8%D1%81%D0%BE%D0%BA_%D0%B2%D0%BE%D0%BE%D1%80%D1%83%D0%B6%D0%B5%D0%BD%D0%B8%D1%8F_%D0%B8_%D0%B2%D0%BE%D0%B5%D0%BD%D0%BD%D0%BE%D0%B9_%D1%82%D0%B5%D1%85%D0%BD%D0%B8%D0%BA%D0%B8_%D0%A1%D1%83%D1%85%D0%BE%D0%BF%D1%83%D1%82%D0%BD%D1%8B%D1%85_%D0%B2%D0%BE%D0%B9%D1%81%D0%BA_%D0%A0%D0%BE%D1%81%D1%81%D0%B8%D0%B9%D1%81%D0%BA%D0%BE%D0%B9_%D0%A4%D0%B5%D0%B4%D0%B5%D1%80%D0%B0%D1%86%D0%B8%D0%B8')
    but_inline4 = InlineKeyboardButton('Посмотреть статью про танки', url='https://perevozka24.ru/pages/sovremennye-tanki-rossii')
    keyboard_inline2.add(but_inline3, but_inline4)

    return keyboard_inline2