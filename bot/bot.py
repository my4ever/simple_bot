import requests
from time import sleep
import os

TOKEN =

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
    print(update['message']['from']['username'], update['message']['text'])
    message = update['message']['text']
    return message

def send_mess(chat, text):
    """Sending the message."""
    params = {'chat_id': chat, 'text': text}
    response = requests.post(url + 'sendMessage', data=params)
    return response

def checking_for_user(update):
    """Checking for username in database."""
    username = update['message']['from']['username']
    with open('db.txt', 'r') as database:
        names = [name for name in database]
        print(names)
        if username not in names:
            add_user_to_db(username)

def add_user_to_db(username):
    """Adding username into database."""
    with open('db.txt', 'a') as database:
        database.write('\n' + username)

def main():
    update_id = last_update(get_updates_json(url))['update_id']
    while True:
        if update_id == last_update(get_updates_json(url))['update_id']:
           send_mess(get_chat_id(last_update(get_updates_json(url))),
                     get_message(last_update(get_updates_json(url))))
           checking_for_user(last_update(get_updates_json(url)))
           update_id += 1
    sleep(1)

if __name__ == '__main__':
    main()
