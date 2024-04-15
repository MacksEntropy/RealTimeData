import json
import time
import random

from kafka import KafkaProducer
from faker import Faker

from data import fake_transaction

#Module for simulating a Kafka Stream for testing

class MockDataStream():

    def __init__(self) -> None:
        self.fake = Faker()

    def possible_error(self):
        if random.randint(0,10) >= 7:
            return -1
        else:
            return 1

    def fake_transaction(self):
        return {
            "Name": self.fake.name(),
            "Email": self.fake.email(),
            "Price": round(random.uniform(0.0,100.0),2),
            "Quantity": random.randint(0,10),
            "Possible_error": self.possible_error()
        }

    def produce_data(self):
        producer = KafkaProducer(bootstrap_servers='localhost:9092', 
                                value_serializer=lambda m: json.dumps(m).encode("utf-8"))
        print('Producer created..............')
        while 1:
            transaction = self.fake_transaction()
            producer.send('Transactions',transaction)
            time.sleep(5)

if __name__ == '__main__':
    pass