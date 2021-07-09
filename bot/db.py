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

# updateid
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
				print("have to create Table")
				self.cursor.execute(table)
			print("connection closed")
		self.con.close()


		# def save_user(self, telegramid):
		# 	users_list = self.cursor.execute('SELECT * FROM user_instance')
		# 	if telegramid not in users_list:
		# 		self.cursor.execute('') #TODO

		# def


TelegramDB()
