from aiogram import Bot, types
from pathlib import Path
import soundfile as sf
import librosa
import os


async def db_start():
    path = Path("photos/")
    path.mkdir(parents=True, exist_ok=True)
    path = Path("audios/")
    path.mkdir(parents=True, exist_ok=True)


async def save_photo(message: types.Message, bot: Bot):
    #await db_start()
    photo = message.photo[-1]
    user_id = message.from_user.id
    user_str = str(user_id)
    user_path = "photos/" + user_str
    path = Path(user_path)
    path.mkdir(parents=True, exist_ok=True)
    num_files = len(os.listdir(path=path))
    filename = f'{user_str}_{str(num_files)}.jpg'
    full_filename = os.path.join(path, filename)
    await bot.download(photo, destination=full_filename)


async def save_audio(message: types.Message, bot: Bot):
    SAMPLERATE = 16000
    if message.audio:
        audio = message.audio
    elif message.voice:
        audio = message.voice
    user_id = message.from_user.id
    user_str = str(user_id)
    user_path = "audios/" + user_str
    path = Path(user_path)
    path.mkdir(parents=True, exist_ok=True)
    num_files = len(os.listdir(path=path))
    filename = f'{user_str}_{str(num_files)}.ogg'
    full_filename = os.path.join(path, filename)
    await bot.download(audio, destination=full_filename)
    data, samplerate = librosa.load(full_filename, sr=SAMPLERATE)
    sf.write(full_filename[:-3] + 'wav', data, SAMPLERATE)
    os.remove(full_filename)
