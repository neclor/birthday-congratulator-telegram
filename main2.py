import asyncio
import time
import logging
from telethon.sync import TelegramClient, events
from datetime import datetime


from bot import *
from birthday_manager import *


logging.basicConfig(
	#filename = "bot.log",
	level = logging.INFO,
	format = "[%(levelname)s %(asctime)s] %(name)s: %(message)s",
	datefmt='%Y-%m-%d %H:%M:%S',
	handlers = [
		logging.FileHandler("bot.log"),
		logging.StreamHandler()])
logger = logging.getLogger(__name__)


def start_bot() -> None:
	with bot:
		logger.info("Bot started")
		while True:
			try:
				logger.info("Try to connect...")
				with bot:
					logger.info("yes")
					bot.run_until_disconnected()
			except Exception as e:
				logger.warning(e)
				logger.info("Wait 10 sec ...")
				time.sleep(10)


async def main() -> None:
	logger.info("Connected")
	logger.info("Start sending messages")

	while True:
		try:
			if not bot.is_connected():
				logger.info("Try to connect ...")
				await bot.connect()

			await bot.send_message("me", "test")
			logger.info("Message sent")
			logger.info("Wait 10 sec ...")

			await asyncio.sleep(10)

		except Exception as e:
			logger.error(e)
			logger.warning("Message sending error")
			logger.info("Wait 10 sec ...")
			time.sleep(10)





'''
def aaaa():
	birthdays: list[dict] = get_birthdays()
	congratulated_today: list[str] = get_congratulated_today()

	for birthday in birthdays:
		if birthday["name"] in congratulated_today:
			pass
'''






if __name__ == "__main__":
	async def clock():
		while True:
			print('The time:', datetime.now())
			await asyncio.sleep(1)

	loop.create_task(clock())
	bot.run_until_disconnected()
