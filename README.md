# Kafka Python Messaging Project

This project demonstrates a simple messaging system using:

- Apache Kafka
- Apache Zookeeper
- Python
- Docker
- Git / GitHub

## Architecture

Producer → Kafka Topic → Consumer

The Python producer sends messages to a Kafka topic and the consumer reads and processes them.

## Technologies Used

- Apache Kafka
- Apache Zookeeper
- Python
- Docker
- Git

## Project Structure

```
kafka-python-project
│
├── docker-compose.yml
├── requirements.txt
│
├── producer
│   └── producer.py
│
└── consumer
    └── consumer.py
```

## Setup Instructions

### 1 Start Kafka and Zookeeper

```
docker compose up -d
```

### 2 Run Producer

```
python producer/producer.py
```

### 3 Run Consumer

```
python consumer/consumer.py
```

## Example Output

Producer:

```
Sent: {"event": "login"}
```

Consumer:

```
Received: {"event": "login"}
```

## Learning Goals

- Understand Kafka messaging
- Build producer/consumer applications
- Run Kafka using Docker
- Use Git and GitHub for version control