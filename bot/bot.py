import requests

MAIN_URL = f'https://api.telegram.org/bot{TOKEN}'

def get_update():
    """Getting update for server."""
    while True:
        r = requests.get(f'{MAIN_URL}/getUpdates').json()
        print(r)
        # print(len(r))
        # if r['massege_id'] >
        # answer = {
        #     'chat_id': 2323,
        #     'text': ''
        # }

def reversing_msg():
    """Reversing original message."""
    pass

def send_msg(answer):
    """Sending answer"""
    r = requests.post(f'{MAIN_URL}/sendMessage', data=answer)

get_update()
