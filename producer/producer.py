from kafka import KafkaProducer
import json
import time
import random

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

events = ["login", "logout", "purchase", "payment"]

while True:
    message = {
        "event": random.choice(events)
    }

    producer.send("demo_topic", message)
    print("Sent:", message)

    time.sleep(2)