import logging
import csv
import datetime
from datetime import datetime


logger = logging.getLogger(__name__)


BIRTHDAY_DATA: str = "birthdays_data.csv"


def get_birthdays() -> list[dict]:
	try:
		with open(BIRTHDAY_DATA, "r", newline = "") as birthdays_data:
			birthdays: csv.DictReader = csv.DictReader(birthdays_data)
			return list(birthdays)
	except Exception as e:
		logger.error(e)
		raise Exception(e)



def change_birthday(name: str, new_birthday: dict) -> None:
	try:
		birthdays: list[dict] = get_birthdays()
		for birthday in birthdays:
			if birthday["name"] == name:


	except:
		pass





def add_bithday(birthday: dict) -> None:

    pass


def delete_birthday(name: str) -> None:
	pass
