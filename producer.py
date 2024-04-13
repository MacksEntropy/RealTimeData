import json
from kafka import KafkaProducer
from data import fake_transaction
import time

#Module for simulating a Kafka Stream for testing

def produce_data():
    producer = KafkaProducer(bootstrap_servers='localhost:9092', 
                            value_serializer=lambda m: json.dumps(m).encode("utf-8"))
    print('Producer created..............')
    while 1:
        transaction = fake_transaction()
        producer.send('Transactions',transaction)
        time.sleep(5)

if __name__ == '__main__':
    produce_data()