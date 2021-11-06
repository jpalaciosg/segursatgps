import redis
import json
import requests

URL = 'http://sos.segursat.com:8080/alertcenter/insert-data/'

items = []

redisClient = redis.StrictRedis(host='localhost',port=6379,db=0)
while(redisClient.llen('ssatAlertQueue')!=0):
    item = redisClient.lpop('ssatAlertQueue')
    item = json.loads(item)
    items.append(item)

for item in items:
    headers = {
      'Content-Type': 'application/json; charset=utf-8',
    }
    response = requests.post(URL,headers=headers,data=json.dumps(item))
    print(response.status_code)
    print(response.text)
    print('==============')
