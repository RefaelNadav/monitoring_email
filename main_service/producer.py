from kafka import KafkaProducer
import json


# Kafka producer setup
producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)



def produce_email(data):

    producer.send('messages.all', value=data)
    print(f"Produced email: {data}")