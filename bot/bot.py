import requests

from time import sleep

import db

TOKEN = None
with open('/home/ruslan/Dev/simple_projects/simple_bot/.env', 'r') as token:
    for i in token:
        TOKEN = str(i)
url = f'https://api.telegram.org/bot{TOKEN}/'

final_respose = "Спасибо, вопросов больше нет."

def get_updates_json(request):
    """Getting update from server."""
    response = requests.get(request + 'getUpdates')
    return response.json()

def last_update(data):
    """Getting last update info."""
    results = data['result']
    total_updates = len(results) - 1
    return results[total_updates]

def check_update_id(data):
    """Checking for updateid in DB."""
    results = data['result']
    for i in results:
        update_id = str(i['update_id'])
        return update_id

def get_chat_id(massage):
    """Getting chat id."""
    chat_id = massage['message']['chat']['id']
    return chat_id

def get_message(massage):
    """Getting message."""
    message = massage['message']['text']
    return message

def get_telegramid(massage):
    """Getting user id."""
    telegramid = str(massage['message']['from']['id'])
    return telegramid

def get_username(massage):
    """Getimg username."""
    username = massage['message']['from']['first_name']
    return username

def send_message(chat, text):
    """Sending the message."""
    params = {'chat_id': chat, 'text': text}
    response = requests.post(url + 'sendMessage', data=params)
    return response

def checking_for_user(update):
    """Checking for username in database."""
    telegramid = get_telegramid(update)
    username = update['message']['from']['username']
    check_for_user_db(telegramid, username)

def main():
    data = get_updates_json(url)
    if db.check_last_updateid_db() is None:
        update_id = db.add_update_id_db(check_update_id(data[-1]))
        print(update_id)
    else:
        update_id = db.check_last_updateid_db()
    while True:
        if int(update_id) != last_update(data)['update_id']:
            print('We hava a new massages!')
            for massage in data['result']:
                massage_id = str(massage['update_id'])
                if db.check_on_update_db(massage_id) is None:
                    username = get_username(massage)
                    telegramid = get_telegramid(massage)
                    # adding id into db
                    db.add_update_id_db(massage_id)
                    # checking for user in db
                    if db.check_for_user_db(telegramid, username) is None:
                        db.save_user_db(telegramid, username)
                    # getting question id and the question
                    questionid = db.check_for_questionid_db(telegramid)
                    if questionid <= db.get_amout_of_questions_db():
                        question = db.look_for_question_db(telegramid, questionid)
                        # compering ansewer with variants
                        answers = db.get_variants_of_answers_db(questionid)
                        answer = get_message(massage).lower()
                        if answer in answers:
                            print('saving answer!')
                            answer_id = db.get_answer_id_db(answer)
                            # adding user answer into db
                            db.save_answer_db(telegramid, questionid, answer_id)
                            # updating question id in user instance
                            db.update_questionid_userinstance_db(telegramid, questionid)
                            questionid = db.check_for_questionid_db(telegramid)
                            question = db.look_for_question_db(telegramid, questionid)
                            answers = db.get_variants_of_answers_db(questionid)
                        # senging massage 
                        chat_id = get_chat_id(massage)
                        send_message(chat_id, question)
                        for i in answers:
                            send_message(chat_id, i.capitalize())
                        # setting new update id
                        update_id = db.check_last_updateid_db() 
                    else:
                        chat_id = get_chat_id(massage)
                        send_message(chat_id, final_respose)
                        update_id = db.check_last_updateid_db() 
        else:
            print('No new massages')
            data = get_updates_json(url)
        sleep(1)


if __name__ == '__main__':
    main()
