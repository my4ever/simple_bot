import requests

from time import sleep

from db import check_for_user_db, send_question_db

TOKEN = None
with open('/home/ruslan/Dev/simple_projects/simple_bot/.env', 'r') as token:
    for i in token:
        TOKEN = str(i)
url = f'https://api.telegram.org/bot{TOKEN}/'


def get_updates_json(request):
    """Getting update from server."""
    response = requests.get(request + 'getUpdates')
    return response.json()


def last_update(data):
    """Getting last update info."""
    results = data['result']
    total_updates = len(results) - 1
    return results[total_updates]


def get_chat_id(update):
    """Getting chat id."""
    chat_id = update['message']['chat']['id']
    return chat_id


def get_message(update):
    """Getting message."""
    message = update['message']['text']
    return message

def get_telegramid(update):
    """Getting user id."""
    telegramid = str(update['message']['from']['id'])
    return telegramid


def send_message(chat, text):
    """Sending the message."""
    text = send_question_db()
    params = {'chat_id': chat, 'text': text}
    response = requests.post(url + 'sendMessage', data=params)
    return response


def checking_for_user(update):
    """Checking for username in database."""
    telegramid = get_telegramid(update)
    username = update['message']['from']['username']
    check_for_user_db(telegramid, username)

def main():
    update_id = last_update(get_updates_json(url))['update_id']
    while True:
        if update_id == last_update(get_updates_json(url))['update_id']:
           send_message(
               get_chat_id(last_update(get_updates_json(url))),
               get_message(last_update(get_updates_json(url))))
           checking_for_user(last_update(get_updates_json(url)))
           update_id += 1
    sleep(5)


if __name__ == '__main__':
    main()
