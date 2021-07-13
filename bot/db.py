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

question_id_default = 1 # needed when adding user into DB

def connect_to_db():
	db = sqlite3.connect('./db/telegram.db')
	cursor = db.cursor()
	return db, cursor

def check_for_user_db(telegramid, username):
	"""Checking for user existens in database."""
	db, cursor = connect_to_db()
	user_instance = cursor.execute(
		'SELECT telegramid FROM user_instance '
		f'WHERE telegramid="{telegramid}"'
		).fetchone()
	return user_instance

	# if users_list:
	# 	check_for_question_db(telegramid)
	# else:
	# 	save_user_db(telegramid, username)
	
def save_user_db(telegramid, username):
	"""Adding user into database."""
	db, cursor = connect_to_db()
	SQL = """INSERT INTO user_instance
			 (telegramid, username, lastquestionid, regestrydate)
			 VALUES(?, ?, ?, ?)"""
	VALUES = (telegramid, username, question_id_default, dt.now())
	cursor.execute(SQL, VALUES)
	db.commit()

	# check_for_question_db(telegramid) # asking user a question. 

def check_for_question_db(telegramid):
	"""Checking for question that user have not answered."""
	db, cursor = connect_to_db()
	question_id = cursor.execute(
		'SELECT lastquestionid FROM user_instance '
		f'WHERE telegramid="{telegramid}"'
		).fetchone()[0]
	return question_id

	# send_question_db(question_id, telegramid)

def look_for_question_db(telegramid, question_id):
	"""Sending the question to the user."""
	db, cursor = connect_to_db()
	question = cursor.execute(
		'SELECT text FROM question '
		f'WHERE id="{question_id}"'
		).fetchone()[0]
	return question

def save_answer_db(telegramid, answer):
	"""Saving answer into datebase."""
	pass

def check_on_update_db(updateid):
	"""Checking on a new message."""
	db, cursor = connect_to_db()
	upadete_id = cursor.execute(
			'SELECT textid FROM update_id '
			f'WHERE textid="{updateid}"'
		).fetchone()
	return upadete_id

def add_update_id_db(updateid):
	db, cursor = connect_to_db()
	SQL = """INSERT INTO update_id
			 (textid)
			 VALUES(?)"""
	VALUES = updateid
	cursor.execute(SQL, [VALUES])
	db.commit()

def add_question_db(text):
	db, cursor = connect_to_db()
	SQL = """INSERT INTO question
			 (text) 
			 VALUES(?)"""
	VALUES = text 
	cursor.execute(SQL, VALUES)
	cursor.commit()		 
