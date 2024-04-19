import json

from kafka import KafkaConsumer,KafkaProducer
# from cassandra.cluster import Cluster
import pandas as pd

from producer import MockDataStream
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
    df = pd.DataFrame()
    t = 0
    for msg in consumer:
        print(f"New Transaction: {msg.value}")
        # tmp = pd.DataFrame(msg.value,index=[t])
        # t += 1
        # df = pd.concat([df,tmp])

        # Aggregating numeric data
        # agg_table = df.select_dtypes(include=['int64','float64']).sum()
        # results = agg_table.to_json(orient='columns')
        # producer.send('Topic_A',results)

        #Sending results to cassandra, untested but should work
        # cluster = Cluster(ip_address)
        # session = cluster.connect(keyspace_name)
        # query = "INSERT INTO data(Name,Email,Price,Quantity,Possible_error) VALUES (?,?,?,?,?)"
        # prepared = session.prepare(query)
        # for item in df:
        #     session.execute(prepared, (item.Name_value,item.Email_value,item.Price_value,item.Quantity_value,item.Possible_error_value))

        #Filtering out entries with negative values
        # filtered = df[(df.select_dtypes(include=['int64','float64']) > 0).all(1)]
        # filtered_results = filtered.to_json(orient='columns')
        # producer.send('Topic_B',filtered_results)