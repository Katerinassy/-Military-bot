from aiogram import Bot, Dispatcher, types, executor
from config import TELEGRAM_TOKEN
from keboard.keyboards import get_keyboard_1, get_keyboard_2
from keboard.key_inline import get_keyboard_1_inline, get_keyboard_2_inline
from neiro.neiro_consilt import get_sovet
import requests

bot = Bot(token=TELEGRAM_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands='start')
async def start(message: types.Message):
    await message.answer('Привет, я бот на военную тематику, ты можешь воспользоваться кнопками\n или же задать вопрос напрямую с помощью команды /sovet.', reply_markup=get_keyboard_1())


@dp.message_handler(commands='sovet')
async def analize_message(message:types.Message):
    user = message.get_args()
    response_text = await get_sovet(user)
    await message.answer(response_text)

@dp.message_handler(lambda message: message.text == 'Отправь фото погонов')
async def button_1_click(message: types.Message):
    await bot.send_photo(message.chat.id, photo='https://kirov-portal.ru/upload/original/blog/575/575bf99caf665daf46eda79bc89c8125.jpg', caption='Вот тебе погоны\n но ниже ты можешь ознакомиться с другми погонами', reply_markup=get_keyboard_1_inline())



@dp.message_handler(lambda message: message.text == 'Перейти на следующую клавиатуру')
async def button_2_click(message: types.Message):
    await message.answer('Тут ты можешь попросить бота показать тебе танки.', reply_markup=get_keyboard_2())

# @dp.message_handler(lambda message: message.text == 'Кнопка 4')
# async def button_4_click(message: types.Message):
#     await message.answer('Ты нажал кнопку 2')

@dp.message_handler(lambda message: message.text == 'Отправь фото танка Т-14')
async def button_3_click(message: types.Message):
    await bot.send_photo(message.chat.id, photo='https://www.oficery.ru/wp-content/uploads/2020/08/s1200-2.jpg', caption='Вот тебе танк Т-14\n но ниже ты можешь ознакомиться с другми моделями танков России', reply_markup=get_keyboard_2_inline())

@dp.message_handler(lambda message: message.text == 'Вернуться на 1 клавиатуру')
async def button_2_click(message: types.Message):
    await message.answer('Тут ты можешь попросить бота отправить фото погонов', reply_markup=get_keyboard_1())





if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)