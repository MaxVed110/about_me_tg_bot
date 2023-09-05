import asyncio
import handlers
from aiogram import Bot, Dispatcher


async def main():
    bot = Bot(token='6368801567:AAHqn6pSQW4cnDeSKXnWU40g4ctDBim0UQU')

    dp = Dispatcher()
    dp.include_router(handlers.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
