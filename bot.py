import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command
from dotenv import load_dotenv
import os
from io import BytesIO
from photo_functions import contains_face
import db


# bot object
load_dotenv()
bot = Bot(token=os.getenv('TOKEN'))
# dispatcher
dp = Dispatcher()


async def on_startup():
    await db.db_start()


# handler for the /start command
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    welcome_text = "Hello! This is the SavingStuffBot. It saves audio messages as .wav files and photos with faces"
    await message.answer(welcome_text)


# handler for photos
@dp.message(F.photo)
async def handle_photo(message: types.Message, bot: Bot):
    img_stream = BytesIO()
    await bot.download(message.photo[-1], destination=img_stream)
    if contains_face(img_stream):
        await db.save_photo(message, bot)
    else:
        await message.reply('No face in this photo')


# handler for audio messages
@dp.message(F.voice | F.audio)
async def handle_audio(message: types.Message, bot: Bot):
    await db.save_audio(message, bot)


# Launching polling
async def main():
    await dp.start_polling(bot, on_startup=on_startup)


if __name__ == "__main__":
    asyncio.run(main())