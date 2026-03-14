from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    "demo_topic",
    bootstrap_servers='localhost:9092',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

for message in consumer:
    data = message.value
    print("Received:", data)

    with open("messages.log", "a") as f:
        f.write(str(data) + "\n")