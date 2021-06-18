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
# ython3 manage.py graph_models -a -g -o imaginefile_name.png
# # что бы красиво показать содержимое таблицы
# >>>.header on
# >>>.mode column
# >>>pragma table_info(<tablename>)
# # или не красиво
# >>>.schema <table name>
# # exit from sqlite shell
# >>>.exit



# TEXT, INTEGER, BOOL 0,1
# User
# 	id pk
# 	name txt
# 	phone int
# 	telegramid int
# 	admin bool
# 	regestrydate txt
# 	lastquestionid fk


# Question
# 	id pk
# 	text txt: id-1, text- какой любимый цвет?


# Answer
# 	id pk
# 	questionid fk
# 	text txt : id-1, qfk -1, text-зеленый; id-2, qfk -1, text-красный

# UserAnswer
# 	id pk
# 	userid fk
# 	questionid fk
# 	answerid fk

# !!!! UserMessage
# 	id
# 	userid
# 	pubdate
# 	text
# 	isnew
# 	textanswer
import os
import sqlite3
# from db_tables import CREATE_TABLES_LIST


user_create = ''' CREATE TABLE IF NOT EXISTS user(
				 id INTEGER PRIMARY KEY,
				 telegramid TEXT NOT NULL UNIQUE,
				 phone TEXT DEFAULT "",
				 username TEXT NOT NULL,
				 isadmin INTEGER DEFAULT 0,
				 regestrydate TEXT DEFAULT  "") '''


CREATE_TABLES_LIST = [user_create]

class TelegramDB():

	def __init__(self):
		if not os.path.isdir("./db"):
			os.mkdir("db")
		# connect or create DB
		self.con = sqlite3.connect(os.path.join("db", "telegram.db"))
		# manager class
		self.cursor = self.con.cursor()
		if self.cursor.execute("SELECT name FROM sqlite_master \
							WHERE type='table' AND name='user'").fetchall():
			print("Its ok db exisits")
		else:
			print("have to create Tables")
			self.cursor.execute(user_create)
		print("connection closed")
		self.con.close()


TelegramDB()
