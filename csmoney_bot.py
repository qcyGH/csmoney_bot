from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
from aiogram.utils.markdown import hbold, hlink
from main import collect_data
from bot_token import *
import time
import json

bot = Bot(token=bot_token, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    start_buttons = ['Ножи 🔪', 'Перчатки 🥊', 'Пистолеты 🔫', 'Пистолеты-пулемёты 🔫', 'Штурмовые винтовки 🔫', 'Снайперские винтовки 💥', 'Дробовики 💥', 'Пулемёты 🔫']
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*start_buttons)

    await message.answer('Выберите категорию', reply_markup=keyboard)

@dp.message_handler(Text(equals='Ножи 🔪'))
async def get_discount_knives(message: types.Message):
    await message.answer('Подождите немного. Провожу анализ...')

    collect_data(weapont_type=2, minPrice=2000)

    with open('result.json', encoding="utf-8") as file:
        data = json.load(file)

    count_result = 0
    for index, item in enumerate(data):
        card = f'{hlink(item.get("full_name"), item.get("3d"))}\n' \
               f'{hbold("Скидка: ")}{item.get("overprice")}%\n' \
               f'{hbold("Цена: ")}${item.get("item_price")}'
        count_result += 1
        if index%20 == 0:
            time.sleep(3)

        await message.answer(card) 
    await message.answer(f'Найдено {count_result} позиций 🔥')
    await message.answer('Удачных покупок 😉')

@dp.message_handler(Text(equals='Перчатки 🥊'))
async def get_discount_knives(message: types.Message):
    await message.answer('Подождите немного. Провожу анализ...')

    collect_data(weapont_type=13, minPrice=1200)

    with open('result.json', encoding="utf-8") as file:
        data = json.load(file)

    count_result = 0
    for index, item in enumerate(data):
        card = f'{hlink(item.get("full_name"), item.get("3d"))}\n' \
               f'{hbold("Скидка: ")}{item.get("overprice")}%\n' \
               f'{hbold("Цена: ")}${item.get("item_price")}'
        count_result += 1
        if index%20 == 0:
            time.sleep(3)

        await message.answer(card) 
    await message.answer(f'Найдено {count_result} позиций 🔥')
    await message.answer('Удачных покупок 😉')

@dp.message_handler(Text(equals='Пистолеты 🔫'))
async def get_discount_knives(message: types.Message):
    await message.answer('Подождите немного. Провожу анализ...')

    collect_data(weapont_type=5, minPrice=500)

    with open('result.json', encoding="utf-8") as file:
        data = json.load(file)

    count_result = 0
    for index, item in enumerate(data):
        card = f'{hlink(item.get("full_name"), item.get("3d"))}\n' \
               f'{hbold("Скидка: ")}{item.get("overprice")}%\n' \
               f'{hbold("Цена: ")}${item.get("item_price")}'
        count_result += 1
        if index%20 == 0:
            time.sleep(3)

        await message.answer(card) 
    await message.answer(f'Найдено {count_result} позиций 🔥')
    await message.answer('Удачных покупок 😉')

@dp.message_handler(Text(equals='Пистолеты-пулемёты 🔫'))
async def get_discount_knives(message: types.Message):
    await message.answer('Подождите немного. Провожу анализ...')

    collect_data(weapont_type=6, minPrice=100)

    with open('result.json', encoding="utf-8") as file:
        data = json.load(file)

    count_result = 0
    for index, item in enumerate(data):
        card = f'{hlink(item.get("full_name"), item.get("3d"))}\n' \
               f'{hbold("Скидка: ")}{item.get("overprice")}%\n' \
               f'{hbold("Цена: ")}${item.get("item_price")}'
        count_result += 1
        if index%20 == 0:
            time.sleep(3)

        await message.answer(card) 
    await message.answer(f'Найдено {count_result} позиций 🔥')
    await message.answer('Удачных покупок 😉')

@dp.message_handler(Text(equals='Штурмовые винтовки 🔫'))
async def get_discount_knives(message: types.Message):
    await message.answer('Подождите немного. Провожу анализ...')

    collect_data(weapont_type=3, minPrice=2000)

    with open('result.json', encoding="utf-8") as file:
        data = json.load(file)

    count_result = 0
    for index, item in enumerate(data):
        card = f'{hlink(item.get("full_name"), item.get("3d"))}\n' \
               f'{hbold("Скидка: ")}{item.get("overprice")}%\n' \
               f'{hbold("Цена: ")}${item.get("item_price")}'
        count_result += 1
        if index%20 == 0:
            time.sleep(3)

        await message.answer(card) 
    await message.answer(f'Найдено {count_result} позиций 🔥')
    await message.answer('Удачных покупок 😉')                      

@dp.message_handler(Text(equals='Снайперские винтовки 💥'))
async def get_discount_knives(message: types.Message):
    await message.answer('Подождите немного. Провожу анализ...')

    collect_data(weapont_type=4, minPrice=2000)

    with open('result.json', encoding="utf-8") as file:
        data = json.load(file)

    count_result = 0
    for index, item in enumerate(data):
        card = f'{hlink(item.get("full_name"), item.get("3d"))}\n' \
               f'{hbold("Скидка: ")}{item.get("overprice")}%\n' \
               f'{hbold("Цена: ")}${item.get("item_price")}'
        count_result += 1
        if index%20 == 0:
            time.sleep(3)

        await message.answer(card) 
    await message.answer(f'Найдено {count_result} позиций 🔥')
    await message.answer('Удачных покупок 😉')

@dp.message_handler(Text(equals='Дробовики 💥'))
async def get_discount_knives(message: types.Message):
    await message.answer('Подождите немного. Провожу анализ...')

    collect_data(weapont_type=7, minPrice=50)

    with open('result.json', encoding="utf-8") as file:
        data = json.load(file)

    count_result = 0
    for index, item in enumerate(data):
        card = f'{hlink(item.get("full_name"), item.get("3d"))}\n' \
               f'{hbold("Скидка: ")}{item.get("overprice")}%\n' \
               f'{hbold("Цена: ")}${item.get("item_price")}'
        count_result += 1
        if index%20 == 0:
            time.sleep(3)

        await message.answer(card) 
    await message.answer(f'Найдено {count_result} позиций 🔥')
    await message.answer('Удачных покупок 😉')

@dp.message_handler(Text(equals='Пулемёты 🔫'))
async def get_discount_knives(message: types.Message):
    await message.answer('Подождите немного. Провожу анализ...')

    collect_data(weapont_type=8, minPrice=20)

    with open('result.json', encoding="utf-8") as file:
        data = json.load(file)

    count_result = 0
    for index, item in enumerate(data):
        card = f'{hlink(item.get("full_name"), item.get("3d"))}\n' \
               f'{hbold("Скидка: ")}{item.get("overprice")}%\n' \
               f'{hbold("Цена: ")}${item.get("item_price")}'
        count_result += 1
        if index%20 == 0:
            time.sleep(3)

        await message.answer(card) 
    await message.answer(f'Найдено {count_result} позиций 🔥')
    await message.answer('Удачных покупок 😉')                                  
            

def main():
    executor.start_polling(dp)

if __name__ == '__main__':
    main()       