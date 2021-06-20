user_instance = ''' CREATE TABLE IF NOT EXISTS user(
                    id INTEGER PRIMARY KEY,
				    telegramid TEXT NOT NULL UNIQUE,
				    phone TEXT DEFAULT "",
				    username TEXT NOT NULL,
				    isadmin INTEGER DEFAULT 0,
				    regestrydate TEXT DEFAULT  ""
				    ) '''

question = ''' CREATE TABLE IF NOT EXISTS question(
			   id INTEGER PRIMARY KEY,
			   text TEXT NOT NULL DEFAULT ""
			   ) '''

answer = ''' CREATE TABLE IF NOT EXISTS answer(
			 id INTEGER PRIMARY KEY,
			 text TEXT DEFAULT "",
			 questionid INTEGER NOT NULL,
			 FOREIGN KEY (questionid) REFERENCES question (id)
			 ) '''

user_answer = '''CREATE TABLE IF NOT EXISTS user_answer(
				id INTEGER PRIMARY KEY,
				userid INTEGER NOT NULL,
				FOREIGN KEY (userid) REFERENCES user_instance (id),
				answerid INTEGER NOT NULL,
				FOREIGN KEY (answerid) REFERENCES answer (id),
				questionid INTEGER NOT NULL,
			    FOREIGN KEY (questionid) REFERENCES question (id)
				) '''

CREATE_TABLES_LIST = [user_instance, question, answer, user_answer]
