from kafka import KafkaConsumer, KafkaProducer
import json

# Kafka consumer and producer setup
consumer = KafkaConsumer(
    'messages.all',
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='earliest',
    group_id='all_messages_processor_group',
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

def is_hostage(email):
    sentences = email.get('sentences')
    for sentence in sentences:
        if 'hostage' in sentence.lower():
            return True
    return False

def is_explosive(email):
    sentences = email.get('sentences')
    for sentence in sentences:
        if 'explos' in sentence.lower():
            return True
    return False

for message in consumer:
    email = message.value

    print("Received message:", email)
    # producer.send('all_messages', email)
    if is_hostage(email):
        producer.send('messages.hostage', value=email)
        print(f"Suspicious content message: {email}")
    elif is_explosive(email):
        producer.send('messages.explosive', value=email)
        print(f"Suspicious content message: {email}")
