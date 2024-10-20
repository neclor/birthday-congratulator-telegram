import logging
import csv
from datetime import datetime
from telethon.sync import TelegramClient, events
from api_data import *


logging.basicConfig(
	filename = MY_SESSION_NAME + ".log",
	level = logging.INFO,
	format = "%(asctime)s %(name)s %(levelname)s %(message)s",
	datefmt='%Y-%m-%d %H:%M:%S',
)
logger = logging.getLogger(__name__)


bot: TelegramClient = TelegramClient(MY_SESSION_NAME, API_ID, API_HASH)


@bot.on(events.NewMessage(pattern = "/start"))
async def start(event):
	await event.respond("Commands:\n/addperson\n/delperson")




@bot.on(events.NewMessage(pattern = "/addperson"))
async def aaaa(event):
	await event.respond("Commands:\n/addperson\n/delperson")



def main() -> None:
	logger.info("dsdasdadad")



	with bot:
		bot.send_message("me", 'ку')




		bot.run_until_disconnected()


def today():
	pass


def send_message():
	pass


if __name__== "__main__":
	main()
