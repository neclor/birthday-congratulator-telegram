from telethon.sync import TelegramClient, events
from api_data import *


bot: TelegramClient = TelegramClient(MY_SESSION_NAME, API_ID, API_HASH)



@bot.on(events.NewMessage(pattern = "/start"))
async def start(event):
	await event.respond("Birthday commands:\n/add - add new birthday\n/remove - delete birthday")


@bot.on(events.NewMessage(pattern = "/add"))
async def add_birthday(event):
	await event.respond("")


@bot.on(events.NewMessage(pattern = "/remove"))
async def remove_birthday(event):
	await event.respond("")






async def connection():
	while True:
		try:
			await bot.run_until_disconnected()
		except (FloodWait, SessionPasswordNeededError, RPCError) as e:
			print(f"Ошибка: {e}. Ожидание перед повторной попыткой...")
			await asyncio.sleep(10)  # Ожидание перед повторным подключением
		except Exception as e:
			print(f"Неожиданная ошибка: {e}. Ожидание перед повторной попыткой...")
			await asyncio.sleep(10)  # Ожидание перед повторным подключением










def today():
	pass


def send_message():
	pass
