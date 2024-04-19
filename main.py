import json

from kafka import KafkaConsumer,KafkaProducer
# from cassandra.cluster import Cluster

from model import Measurement
#Begin by running producer.py, then run main.py to simulate tapping into an existing stream of JSON data

class RealTimeData():

    def __init__(self) -> None:
        pass

if __name__ == "__main__":
    producer = KafkaProducer(bootstrap_servers='localhost:9092', value_serializer=lambda m: json.dumps(m).encode("utf-8"))
    # stream = MockDataStream()
    # stream.produce_data()
    consumer = KafkaConsumer('Measurements',bootstrap_servers='localhost:9092',auto_offset_reset='earliest', value_deserializer=lambda m: json.loads(m.decode('utf-8')))
    print("Starting Consumer.............")
    t = 0
    for msg in consumer:
        m = Measurement(**msg.value)
        print(m)