import speech_recognition as sr

from aiogram import types, F, Router
from aiogram.filters.command import Command
from aiogram.types import FSInputFile
from aiogram.utils.keyboard import ReplyKeyboardBuilder

router = Router()


# заготовка для честной обработки гс
# r = sr.Recognizer()
# def recognise(filename):
#     with sr.AudioFile(filename) as source:
#         audio_text = r.listen(source)
#         try:
#             text = r.recognize_google(audio_text, language='ru_Ru')
#             print(text)
#             return text
#         except Exception:
#             print('Sorry.. run again...')
#             return "Sorry.. run again..."


# приветственное сообщение
@router.message(Command('start'))
async def start_command(message: types.Message):
    kb = [
        [types.KeyboardButton(text="Инструкция")],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True)
    text = 'Привет! Этот бот создан для тестового задания Яндекс в целях знакомства со мной\n\n' \
           'Чтобы узнать его возможности - нажми на кнопку "Инструкция"'
    await message.answer(text, reply_markup=keyboard)


# инструкция
@router.message(F.text.lower() == "инструкция")
async def instruction(message: types.Message):
    text = 'Для получения информации, представленной на кнопках - жми на кнопки.\n' \
           'Для получения дополнительной информации воспользуйся следующими кнопками:\n' \
           '/selfie - посмотреть последнее селфи \n' \
           '/school - посмотреть фото в старших классах \n' \
           '/hobby - почитать историю о хобби \n' \
           'Для получения ссылки на репо с исходным кодом отправь голосовое сообщение со словом\n' \
           '"исходники"'

    builder = ReplyKeyboardBuilder()
    builder.row(types.KeyboardButton(text="Что такое ChatGPT"),
                types.KeyboardButton(text="Отличие SQL от NoSQL"),
                types.KeyboardButton(text="Ода о первой любви"))
    builder.row(types.KeyboardButton(text="Инструкция"))

    await message.answer(text, reply_markup=builder.as_markup(resize_keyboard=True))


# Посмотреть селфи
@router.message(Command('selfie'))
async def upload_photo(message: types.Message):
    image = FSInputFile("./photo/selfie.jpg")
    await message.answer_photo(image)


# Посмотреть фотку из школы
@router.message(Command('school'))
async def upload_photo(message: types.Message):
    image = FSInputFile("./photo/school.jpg")
    await message.answer_photo(image)


# Пост о главном увлечении
@router.message(Command('hobby'))
async def hobby_story(message: types.Message):
    text = 'Как ни странно, но в старших классах и на первых курсах института моим основным увлечением, позволяющим ' \
           'хорошо отдохнуть и провести время с пользой, был страйкбол.\n' \
           'Страйкбол - это военно-тактическая игра, целью которой является популяризация патриотических настроений в' \
           'обществе, совершенствование своих физических и моральных качеств, а также сплачивание коллективов.\n' \
           'Страйкбол - игра друзей :)'
    image = FSInputFile('./photo/hobby.png')
    await message.answer_photo(image, caption=text)


# Что такое ChatGPT
@router.message(F.text.lower() == "что такое chatgpt")
async def what_is_gpt(message: types.Message):
    voice = FSInputFile('./voices/chatGPT.ogg')
    await message.answer_voice(voice)


# Отличие SQL от NoSQL
@router.message(F.text.lower() == "отличие sql от nosql")
async def difference(message: types.Message):
    voice = FSInputFile('./voices/sql.ogg')
    await message.answer_voice(voice)


# Ода о первой любви
@router.message(F.text.lower() == "ода о первой любви")
async def love_story(message: types.Message):
    voice = FSInputFile('./voices/love.ogg')
    await message.answer_voice(voice)


# ссылка на репо
@router.message(F.voice)
async def contact(message: types.Message):
    link = 'Отличный выбор! Вот ссылка на мой GitHub:\nhttps://github.com/MaxVed110/about_me_tg_bot'
    await message.answer(link)
