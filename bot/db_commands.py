import sqlite3


db = sqlite3.connect('./db/telegram.db')
cursor = db.cursor()

def check_for_user(user_id):
	pass

def check_for_answer(user_id):
	pass

def insert_user_answer(user_id, answer):
	pass

def add_user_to_db(user_id, username):
	pass
