from aiogram import Bot, types
from pathlib import Path
import soundfile as sf
import librosa
import os
import config


async def db_start():
    path = Path("photos/")
    path.mkdir(parents=True, exist_ok=True)
    path = Path("audios/")
    path.mkdir(parents=True, exist_ok=True)


async def save_photo(message: types.Message, bot: Bot):
    try:
        photo = message.photo[-1]
        user_id = message.from_user.id
        path = Path(f"photos/{user_id}")
        path.mkdir(parents=True, exist_ok=True)
        num_files = len(os.listdir(path=path))
        filename = f'{user_id}_{str(num_files)}.jpg'
        full_filename = os.path.join(path, filename)
        await bot.download(photo, destination=full_filename)
        await message.reply('Photo with a face saved')
    except Exception as exc:
        print(exc)
        await message.reply('Sorry, something went wrong')


async def save_audio(message: types.Message, bot: Bot):
    try:
        necessary_samplerate = config.SAMPLERATE
        if message.audio:
            audio = message.audio
        elif message.voice:
            audio = message.voice
        user_id = message.from_user.id
        path = Path(f"audios/{user_id}")
        path.mkdir(parents=True, exist_ok=True)
        num_files = len(os.listdir(path=path))
        filename = f'{user_id}_{str(num_files)}.ogg'
        full_filename = os.path.join(path, filename)
        await bot.download(audio, destination=full_filename)
        data, samplerate = librosa.load(full_filename, sr=necessary_samplerate)
        wav_filename = full_filename[:-3] + 'wav'
        sf.write(wav_filename, data, necessary_samplerate)
        os.remove(full_filename)
        await message.reply('Audio saved as a .wav file')
    except Exception as exc:
        print(exc)
        await message.reply('Sorry, something went wrong')
