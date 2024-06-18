import logging
from db import Database
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = "7450181024:AAHK4U9bJ5Pcbib3GoluxgHdo2uu87ieL08"


# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def send_welcome(message: types.Message):
    ful_name = message.from_user.full_name
    user_id = message.from_user.id
    username = message.from_user.username
    query = f"INSERT INTO users_2 (username, full_name, user_id) VALUES ('{username}', '{ful_name}', {user_id})"
    if await Database.check_user_id(user_id):
        await message.reply(f"Assalomu aleykum sizni ko'rganimdan xursantman  {ful_name}")

    else:
        await Database.connect(query, "insert")
        await message.reply(f"Xushkelibsiz {ful_name}")


@dp.message_handler()
async def talk(message: types.Message):
    await message.answer(message.text)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)

