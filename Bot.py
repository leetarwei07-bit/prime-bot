import asyncio
import os
from aiogram import Bot, Dispatcher, types
from aiogram.types import FSInputFile, InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from aiogram.filters import CommandStart

TOKEN = os.environ.get("BOT_TOKEN", "")
WEBAPP_URL = os.environ.get("WEBAPP_URL", "https://your-miniapp-site.com")

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def start_handler(message: types.Message):
    photo = FSInputFile("image.jpg")

    user_name = message.from_user.first_name if message.from_user.first_name else "друг"

    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="🚀 Открыть приложение",
                    web_app=WebAppInfo(url=WEBAPP_URL)
                )
            ]
        ]
    )

    caption = (
        f"👋 Добро пожаловать в PRIME, <b>{user_name}</b>!\n\n"
        "✨ Открой наше мини-приложение и начни знакомство прямо сейчас 👇"
    )

    await message.answer_photo(
        photo=photo,
        caption=caption,
        parse_mode="HTML",
        reply_markup=keyboard
    )


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
