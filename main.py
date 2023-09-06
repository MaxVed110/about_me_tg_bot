import asyncio
import handlers
from aiogram import Bot, Dispatcher


async def main():
    with open('token.txt', 'r') as f:
        token = f.read()

    bot = Bot(token=token)

    dp = Dispatcher()
    dp.include_router(handlers.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
