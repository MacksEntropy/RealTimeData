import json
import time
import random

from kafka import KafkaProducer


class MockDataStream():

    def __init__(self) -> None:
        pass
        
    def mock_chem_levels(self):
        return {
        "H2S_level" : round(random.uniform(0.0,4.0),3),
        "H2O_level" : round(random.uniform(0.0,120.0),3),
        "CO2_level" : round(random.uniform(0.0,3.0),3)
    }

    def mock_measusrements(self):
        return {
        "temperature" : round(random.uniform(10.0,16.0),3),
        "preassure" : round(random.uniform(200.0,1500.0),3),
        "chemical_measurements" : self.mock_chem_levels(),
        "btu_measurement" : round(random.uniform(1000.0,10000.0),3),
        "sensor_id" : random.randint(0,99)
    }

    def produce_data(self):
        producer = KafkaProducer(bootstrap_servers='localhost:9092', 
                                value_serializer=lambda m: json.dumps(m).encode("utf-8"))
        print('Producer created..............')
        while 1:
            measurement = self.mock_measusrements()
            producer.send('Measurements',measurement)
            time.sleep(5)

if __name__ == '__main__':
    
    stream = MockDataStream()
    stream.produce_data()