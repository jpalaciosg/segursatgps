from forwarders.models import Forwarder
from units.models import Device

import pika
import ssl
import json

class PositionForwarder:

    def run(self,unit,position):
        """
        global pika
        global ssl
        global json
        """
        if unit.sutran_process:
            try:
                ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
                ssl_context.set_ciphers('ECDHE+AESGCM:!ECDSA')
                url = f"amqps://replica:oHz5&4CWR4H&qxx6@b-73148309-3f7e-4f49-961e-ed40bb9c8221.mq.us-east-1.amazonaws.com:5671"
                parameters = pika.URLParameters(url)
                parameters.ssl_options = pika.SSLOptions(context=ssl_context)
                connection = pika.BlockingConnection(parameters)
                channel = connection.channel()
                channel.queue_declare(
                    queue='sutran',
                    arguments={
                        'x-message-ttl': 300000
                    }
                )
                channel.basic_publish(
                    exchange='',
                    routing_key='sutran',
                    body=json.dumps(position)
                )
                connection.close()
            except Exception as e:
                print(e)
        if unit.forwarding_enabled:
            forwarders = unit.forwarders.all()
            for forwarder in forwarders:
                if forwarder.is_active:
                    #print(forwarder)
                    try:
                        ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
                        ssl_context.set_ciphers('ECDHE+AESGCM:!ECDSA')
                        url = f"amqps://replica:oHz5&4CWR4H&qxx6@b-73148309-3f7e-4f49-961e-ed40bb9c8221.mq.us-east-1.amazonaws.com:5671"
                        parameters = pika.URLParameters(url)
                        parameters.ssl_options = pika.SSLOptions(context=ssl_context)
                        connection = pika.BlockingConnection(parameters)
                        channel = connection.channel()
                        channel.queue_declare(
                            queue=forwarder.name,
                            arguments={
                                'x-message-ttl': 60000
                            }
                        )
                        channel.basic_publish(
                            exchange='',
                            routing_key=forwarder.name,
                            body=json.dumps(position)
                        )
                        connection.close()
                    except Exception as e:
                        print(e)
"""
pos_forwarder = PositionForwarder()
unit = Device.objects.get(id=12673)
pos_forwarder.run(unit)
"""