from mails.models import AlertMailQueue

import smtplib
import email.utils as email_utils
from datetime import datetime
from email.mime.text import MIMEText
import re

from common.gmt_conversor import GMTConversor

import threading

def thread_function(item):
    global AlertMailQueue
    global smtplib
    global email_utils
    global datetime
    global MIMEText
    global GMTConversor
    global re

    gmt_conversor = GMTConversor()
    now = gmt_conversor.convert_utctolocaltime(datetime.utcnow())
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

    msg_content = f'''
    Estimados señores:

    Se notifica {item.alert_description}.

    - Unidad: {item.unit_name}/{item.unit_description}
    - Fecha y Hora: {item.alert_timestamp}
    - Coordenadas: {item.alert_latitude}/{item.alert_longitude}
    - Velocidad: {item.alert_speed}
    - Direccion: {item.alert_address}
    - Enlace a Google: http://maps.google.com/maps?q={item.alert_latitude},{item.alert_longitude}

    Favor validar esta informacion con el conductor a la brevedad.

    Atentamente,
    Central Segursat
    '''
    msg = MIMEText(msg_content)
    subject = f'NOTIFICACION DE {item.alert_description}'
    msg['Subject'] = subject
    sender = 'alertas@segursat.com'
    msg['From'] = email_utils.formataddr(('Central de Alertas',sender))
    recipients = []
    recipients_temp = item.mails.split(',')
    email_regex = re.compile(r"[^@]+@[^@]+\.[^@]+")
    for rt in recipients_temp:
        if email_regex.match(rt) != None:
            recipients.append(rt)

    msg['To'] = ", ".join(recipients)

    if len(recipients) > 0:
        s = smtplib.SMTP("mail.segursat.com:587")
        s.starttls()
        s.login('alertas@segursat.com','Alertas2020')
        s.sendmail(sender, recipients, msg.as_string())
        s.quit
        item.it_was_sent = 1
        item.save()
        print(f'Thread: {item.id}\n'+\
        '-----------------------------\n'+\
        f'Datetime: {dt_string}\n'+\
        'Payload:\n'+\
        f'{item.alert_description} - {item.unit_name}\n'+\
        'Response:\n'+\
        'OK'+'\n')
    else:
        print(f'Thread: {item.id}\n'+\
        '-----------------------------\n'+\
        f'Datetime: {dt_string}\n'+\
        'Payload:\n'+\
        f'{item.alert_description} - {item.unit_name}\n'+\
        'Response:\n'+\
        'ERROR - NO HAY DESTINATARIOS'+'\n')

queue = AlertMailQueue.objects.filter(it_was_sent=0)

for item in queue:

    x = threading.Thread(target=thread_function, args=(item,))
    x.start()