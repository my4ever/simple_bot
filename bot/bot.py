import requests

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

def check_update_id(data):
    """Checking for update id in DB."""
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
    message = massage['message']['text'].lower()
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

