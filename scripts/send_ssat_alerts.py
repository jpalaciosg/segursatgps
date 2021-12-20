import redis
import json
import requests
from datetime import datetime
import threading

URL = 'http://sos.segursat.com/alertcenter/insert-data/'
items = []

def thread_function(json_payload):
    global requests
    global datetime
    global json
    global URL
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    headers = {
      'Content-Type': 'application/json; charset=utf-8',
    }
    response = requests.post(URL,headers=headers,data=json.dumps(json_payload))
    id = '#'
    print(f'Thread: {id}\n'+\
    '-----------------------------\n'+\
    f'Datetime: {dt_string}\n'+\
    'Payload:\n'+\
    f'{json_payload}\n'+\
    'Response:\n'+\
    response.text+'\n')

redisClient = redis.StrictRedis(host='localhost',port=6379,db=0)
while(redisClient.llen('ssatAlertQueue')!=0):
    item = redisClient.lpop('ssatAlertQueue')
    item = json.loads(item)
    items.append(item)

for item in items:
    x = threading.Thread(target=thread_function, args=(item,))
    x.start()
