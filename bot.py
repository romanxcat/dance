import requests

BOT_TOKEN = "646367082:AAGjM_fSMW9JHltPl_RL08di0MqqQ7VD3aI"

url = "https://api.telegram.org/bot"+BOT_TOKEN+"/"


def get_updates_json(request):  
    response = requests.get(request + 'getUpdates')
    return response.json()


def last_update(data):  
    results = data['result']
    total_updates = len(results) - 1
    return results[total_updates]


def get_chat_id(update):  
    chat_id = update['message']['chat']['id']
    return chat_id

def send_mess(chat, text):  
    params = {'chat_id': chat, 'text': text}
    response = requests.post(url + 'sendMessage', data=params)
    return response

chat_id = get_chat_id(last_update(get_updates_json(url)))
print(chat_id)
#send_mess(chat_id, 'Your message goes here')


#318c6126847f1824a35fb483d4cfffa160f29d0b00afe733a5d7e2fe48746979

