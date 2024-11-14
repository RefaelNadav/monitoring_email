from kafka import KafkaConsumer
import json
from db_config import collection
# from pymongo import MongoClient
#
# # MongoDB setup
# client = MongoClient('mongodb://localhost:27017/')
# db = client['monitor_emails']
# collection = db['all_messages']

# Kafka consumer setup
consumer = KafkaConsumer(
    'messages.all',
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='earliest',
    group_id='all_messages_group',
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

for message in consumer:
    email = message.value
    print(email)
    collection.insert_one(email)
    print(f"Stored message: {email}")