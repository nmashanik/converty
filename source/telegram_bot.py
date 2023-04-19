import os
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

file = open(".secret_token", mode='r')
TOKEN = file.read()[:-1]
file.close()

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def handle_start(msg: types.Message):
    try:
        os.mkdir(f"tmp/{msg.from_user.id}", mode=0o755)
    except FileExistsError:
        pass
    await msg.answer(f"Я бот. Приятно познакомиться {msg.from_user.first_name}")


@dp.message_handler(commands=['stop'])
async def handle_stop(msg: types.Message):
    await msg.answer(f"Goodbye, dear {msg.from_user.first_name}")


@dp.message_handler(commands=['make'])
async def handle_make(msg: types.Message):
    await msg.answer("not implemented")


@dp.message_handler(commands=['reset'])
async def handle_reset(msg: types.Message):
    await msg.answer("not implemented")


@dp.message_handler(commands=['lang'])
async def handle_lang(msg: types.Message):
    await msg.answer("not implemented")


@dp.message_handler(commands=['help'])
async def handle_help(msg: types.Message):
    await msg.answer("Use commands:\n"
                     "/start to launch the bot\n"
                     "/stop to stop the bot\n"
                     "/make to convert files\n"
                     "/reset to forget all uploaded files\n"
                     "/lang to change language\n"
                     "/help to see this message\n")


@dp.message_handler(content_types=['text'])
async def handle_text_message(msg: types.Message):
    mesg = msg.text[::-1]
    await msg.answer(mesg)


@dp.message_handler(content_types=['photo'])
async def handle_photo_message(msg: types.Message):
    fileID = msg.photo[-1].file_id
    file_info = await bot.get_file(fileID)
    downloaded_file = await bot.download_file(file_info.file_path)
    with open(f"tmp/{msg.from_user.id}/{fileID}", "wb") as new_file:
        new_file.write(downloaded_file.getvalue())
    await msg.answer("OK!")


if __name__ == '__main__':
    try:
        os.mkdir("tmp", mode=0o755)
    except FileExistsError:
        pass
    executor.start_polling(dp)
