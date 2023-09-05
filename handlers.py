import asyncio
from aiogram import Bot, Dispatcher, types, F, Router
from aiogram.filters.command import Command

# from config_bot import config
from aiogram.types import FSInputFile

router = Router()


# приветственное сообщение
@router.message(Command('start'))
async def start_command(message: types.Message):
    kb = [
        [types.KeyboardButton(text="Инструкция")],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True)
    await message.answer('Привет!', reply_markup=keyboard)


# инструкция
@router.message(F.text.lower() == "инструкция")
async def instruction(message: types.Message):
    text = 'инструкция и доступные команды на фотки и текст'
    kb = [
        [types.KeyboardButton(text="Что такое ChatGPT"),
         types.KeyboardButton(text="Отличие SQL от NoSQL"),
         types.KeyboardButton(text="Ода о первой любви")],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True)
    await message.answer("Отличный выбор!", reply_markup=keyboard)


# Посмотреть селфи
@router.message(Command('selfie'))
async def upload_photo(message: types.Message):
    image = FSInputFile("./photo/selfie.jpg")
    await message.answer_photo(image)


# Посмотреть фотку из школы
@router.message(Command('shool'))
async def upload_photo(message: types.Message):
    image = FSInputFile("./photo/school.jpg")
    await message.answer_photo(image)


# Пост о главном увлечении
@router.message(Command('hobby'))
async def hobby_story(message: types.Message):
    text = 'История о хобби'
    image = FSInputFile('')
    await message.answer_photo(image, caption=text)


# Что такое ChatGPT
@router.message(Command('gpt'))
async def what_is_gpt(message: types.Message):
    voice = '123'
    await message.answer_voice(voice)


# Отличие SQL от NoSQL
@router.message(Command('dif'))
async def difference(message: types.Message):
    voice = '123'
    await message.answer_voice(voice)


# Ода о первой любви
@router.message(Command('love'))
async def love_story(message: types.Message):
    voice = '123'
    await message.answer_voice(voice)


# ссылка на репо
@router.message(Command('contact'))
async def contact(message: types.Message):
    ...
