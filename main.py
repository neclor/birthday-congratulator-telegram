import logging
from datetime import datetime

from birthday_manager import *

logging.basicConfig(
	filename = "bot.log",
	level = logging.INFO,
	format = "%(asctime)s %(name)s %(levelname)s %(message)s",
	datefmt='%Y-%m-%d %H:%M:%S',
)
logger = logging.getLogger(__name__)


def main() -> None:
	logger.info("Start bot")

	run()



def run() -> None:
	while True:
		birthdays: list[dict] = get_birthdays()













if __name__== "__main__":
	main()
