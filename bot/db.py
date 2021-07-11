# # install browswer
# sudo apt install sqlite3
# # to run sqlite3 browser with more readable info
# sqlite3 -column -header
# # command in sqlite3 shell connect db to input the path
# >>>.open "/home/path/to/dir/db.sqlite3"
# # to see databases
# >>>.databases
# # to see tables
# >>>.tables
# # to see data in tables
# >>>SELECT * FROM <tablename>
# https://sqlitebrowser.org/dl/
# # output sqlite3 bd
# https://superuser.com/questions/313278/pygraphviz-install-on-ubuntu-10-with-django-extensions
# python3 manage.py graph_models -a -g -o imaginefile_name.png
# # что бы красиво показать содержимое таблицы
# >>>.header on
# >>>.mode column
# >>>pragma table_info(<tablename>)
# # или не красиво
# >>>.schema <table name>
# # exit from sqlite shell
# >>>.exit

# updateid Done +
# id int
# textid txt

# while True:
#
# 	data = get
# 	data [{mesa, user1},{mesa, user2}, {mesa, user3}]

# какой ваш любимый цвет
# желтый
# зеленый
# фиолетовый
#
# Страна
# Россия
# Украина
# Белорусия
#
# Сколько вам лет
# до 15
# от 15 -30
# от 31 - 80

# Если пользователь новый - записываем пользователя
# 						  отправляем первый вопрос
# 						  записывает айди вопроса (первого)
#
# Если пользователь старый - проверяем данный ответ сравниваем ответ с нужными ответами
# 					       если ответ устраивает - записываем ответ в базу данных
# 						   записываем айди след. вопроса
# 						   оправляем след вопрос
# 						   если ответ не верный - оправляем повторно вопрос Capitalize


import os
import sqlite3
from datetime import datetime as dt

from sqlite_tables import CREATE_TABLES_LIST


class TelegramDB():

	def __init__(self):
		if not os.path.isdir("./db"):
			os.mkdir("db")
		# connect or create DB
		self.con = sqlite3.connect(os.path.join("db", "telegram.db"))
		# manager class
		self.cursor = self.con.cursor()
		for table in CREATE_TABLES_LIST:
			if self.cursor.execute("SELECT name FROM sqlite_master "
								  f"WHERE type='table' AND name='{table}'").fetchall():
				print("Its ok db exists")
			else:
				print(f"have to create Table: {table.split()[5].strip('(')}")
				self.cursor.execute(table)
			print("connection closed")
		self.con.close()

TelegramDB()

def connect_to_db():
	db = sqlite3.connect('./db/telegram.db')
	cursor = db.cursor()
	return db, cursor

def check_for_user_db(telegramid, username):
	"""Checking for user status in database."""
	db, cursor = connect_to_db()
	users_list =  cursor.execute(
		'SELECT telegramid FROM user_instance'
		)
	if telegramid not in [id[0] for id in users_list]:
		save_user_db(telegramid, username)
	else:
		check_for_question_db(telegramid)

def save_user_db(telegramid, username):
	"""Adding user into database."""
	db, cursor = connect_to_db()
	cursor.execute(
		'INSERT INTO user_instance '
		'(telegramid, username, lastquestionid, regestrydate)'
		f'VALUES("{telegramid}", "{username}", {1}, "{dt.now()}")'
		) 
	db.commit()
	check_for_question_db(telegramid) # asking user a question. 

def check_for_question_db(telegramid):
	"""Checking for question that user have not answered."""
	db, cursor = connect_to_db()
	question_id = cursor.execute(
		'SELECT lastquestionid FROM user_instance '
		f'WHERE telegramid={telegramid}'
		).fetchone()[0]
	send_question_db(question_id, telegramid)


def send_question_db(question_id, telegramid):
	"""Sending the question to the user."""
	db, cursor = connect_to_db()
	question = cursor.execute(
		'SELECT text FROM question '
		f'WHERE id={1}'
		).fetchone()[0]
	return question


def save_answer_db(telegramid, answer):
	"""Saving answer into datebase."""
	pass

def check_on_update_db(updateid):
	"""Checking on a new message."""
	upadete = cursour.execute(
			'SELECT '
		)
	pass

