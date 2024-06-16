from aiogram import Dispatcher, Bot
from aiogram import types

from tgbot.config import load_config

config = load_config("../.env")
WEBHOOK_PATH = f"/{config.tg_bot.token}/"
WEBHOOK_URL = "https://c534-188-113-198-104.ngrok.io"+WEBHOOK_PATH

@app.on_event("startup")
async def on_startup():
    url = await bot.get_webhook_info()
    if url != WEBHOOK_URL:
        await bot.set_webhook(url=WEBHOOK_URL)
        await on_startup_notify(dp)


@app.post(WEBHOOK_PATH)
async def botwebhook(update:dict):
    telegram_update = types.Update(**update)
    Dispatcher.set_current(dp)
    Bot.set_current(bot)
    await dp.process_update(telegram_update)


@app.on_event("shutdown")
async def on_shutdown():
    await bot.get_session().close()


