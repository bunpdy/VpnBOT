import asyncio
import logging
import sys
from aiogram import Bot, Dispatcher
from config import TOKEN
from app.handlers import router

dp = Dispatcher()
bot = Bot(token=TOKEN)

async def main() -> None:
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    try: 
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Exit")
