user_create = ''' CREATE TABLE IF NOT EXISTS user(
				 id INTEGER PRIMARY KEY,
				 telegramid TEXT NOT NULL UNIQUE,
				 phone TEXT DEFAULT "",
				 username TEXT NOT NULL,
				 isadmin INTEGER DEFAULT 0,
				 regestrydate TEXT DEFAULT  ""
				 ) '''

question = ''' CREATE TABLE IF NOT EXISTS question(
			   id INTEGER PRIMARY KEY,
			   text TEXT NOT NULL  ""
			   ) '''

answer = ''' CREATE TABLE IF NOT EXISTS question(
				 id INTEGER PRIMARY KEY,
				 text TEXT DEFAULT "",
				 questionid INTEGER NOT NULL,
				 FOREIGN KEY (questionid) 
				 	REFERENCES question (id)
				 	) '''

useranswer = '''CREATE TABLE IF NOT EXISTS useranswer(
				id INTEGER PRIMARY KEY,
				userid INTEGER NOT NULL,
				FOREIGN KEY (userid)
				 	REFERENCES user_create (id),
				questionid INTEGER NOT NULL,
				FOREIGN KEY (questionid)
					REFERENCES question (id),
				answerid INTEGER NOT NULL,
				FOREIGN KEY (answerid)
					REFERENCES answer (id)
				)'''

CREATE_TABLES_LIST = [user_create, question, answer, useranswer]