from kafka import KafkaConsumer
import json
from db import SessionLocal as session
from models import *
import datetime
import psycopg2

consumer = KafkaConsumer(
    'messages.explosive',
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='earliest',
    group_id='messages_explosive_group',
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

for message in consumer:
    email = message.value



    print("Received message:", email)
    email_address = email.get('email')
    if not email_address:
        continue

    latitude = email['location'].get('latitude')
    longitude = email['location'].get('longitude')
    city = email['location'].get('city')
    country = email['location'].get('country')

    new_location = Location(latitude=latitude, longitude=longitude, city=city, country=country)
    session.add(new_location)

    browser = email['device_info'].get('browser')
    os = email['device_info'].get('os')
    device_id = email['device_info'].get('device_id')

    new_device_info = DeviceInfo(browser=browser, os=os, device_id=device_id)
    session.add(new_device_info)

    username = email.get('username')
    ip_address = email.get('ip_address')
    created_at = email.get('created_at')

    new_email = Email(email_address=email_address, username=username,
                      ip_address=ip_address, created_at=created_at)
    session.add(new_email)

    sentences = email.get('sentences')
    if sentences:
        for sentence in sentences:
            if 'explos' in sentence.lower():
                suspicious_sentence = sentence

                new_sentence_explosive = SuspiciousExplosiveContent(suspicious_sentence=suspicious_sentence,
                                                                    detected_at=datetime.datetime.now())
                session.add(new_sentence_explosive)









