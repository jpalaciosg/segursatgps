import redis
import json
import datetime
import requests

queue_name = 'tracklogSegursatQueue'
gp_username = 'TrackLog'
gp_password = '20segursat20'
items = []

redisClient = redis.StrictRedis(host='localhost',port=6379,db=0)
while(redisClient.llen(queue_name)!=0):
    item = redisClient.lpop(queue_name)
    item = json.loads(item)
    provider = item['provider']
    license_plate = item['unit_name'] 
    timestamp = int(item['timestamp'])
    dt = datetime.datetime.utcfromtimestamp(timestamp)
    dt = dt.strftime("%Y-%m-%dT%H:%M:%S")
    latitude = item['latitude']
    longitude = item['longitude']
    altitude = int(float(item['altitude']))
    speed = int(item['speed'])
    angle = int(item['angle'])
    input_value = 0
    if item['ignition'] == 'true' or item['ignition'] == 1 or item['ignition'] == True:
        input_value = 1

    xml_item = f"""
        <TypeInfo>
          <ExtProviderName>{provider}</ExtProviderName>
          <ExtSerialCode>{license_plate}</ExtSerialCode>
          <Code>{license_plate}</Code>
          <SrcDateTime>{dt}</SrcDateTime>
          <StoryInfo>0</StoryInfo>
          <ST_Status>0</ST_Status>
          <NS_GpsQuality>0</NS_GpsQuality>
          <Flags>0</Flags>
          <Latitude>{latitude}</Latitude>
          <Longitude>{longitude}</Longitude>
          <Altitude>{altitude}</Altitude>
          <Speed>{speed}</Speed>
          <Direction>{angle}</Direction>
          <InputValid>255</InputValid>
          <InputValue>{input_value}</InputValue>
          <FunValid>0</FunValid>
          <FunValue>0</FunValue>
          <OutputValid>255</OutputValid>
          <OutputValue>0</OutputValue>
          <NumAnalogValid>4</NumAnalogValid>
          <AnalogValue0>0</AnalogValue0>
          <AnalogValue1>0</AnalogValue1>
          <AnalogValue2>0</AnalogValue2>
          <AnalogValue3>0</AnalogValue3>
          <Message>data prueba</Message>
        </TypeInfo>
    """
    items.append(xml_item)
    print(xml_item)


xml_header = """<?xml version="1.0" encoding="utf-8"?>
<soap12:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap12="http://www.w3.org/2003/05/soap-envelope">
  <soap12:Body>
    <InsertKFTStoryData xmlns="http://tempuri.org/">
      <AllStories>"""
xml_footer = """</AllStories>
    </InsertKFTStoryData>
  </soap12:Body>
</soap12:Envelope>
"""

if len(items) != 0:
    s = requests.Session()
    url = "http://connector.getposition.com:8099/KFTDataInjector.asmx"
    login_xml = f"<?xml version=\"1.0\" encoding=\"utf-8\"?>\n<soap12:Envelope xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:soap12=\"http://www.w3.org/2003/05/soap-envelope\">\n  <soap12:Body>\n    <LoginWithResponse xmlns=\"http://tempuri.org/\">\n      <UserName>{gp_username}</UserName>\n      <Password>{gp_password}</Password>\n    </LoginWithResponse>\n  </soap12:Body>\n</soap12:Envelope>"
    headers = {
      'Content-Type': 'application/soap+xml; charset=utf-8'
    }
    response = s.post(url,data=login_xml,headers=headers)
    #print(response.text.encode('utf8'))
    payload = ""
    payload += xml_header
    for item in items:
        payload += item
    payload += xml_footer
    headers = {
      'Content-Type': 'text/xml; charset=utf-8'
    }
    #print(payload)
    response = s.post(url,headers=headers,data=payload)
    print(response.text.encode('utf8'))