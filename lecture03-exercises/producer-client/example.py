from time import sleep
from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers=['kafka:9092'])

# input
string = str(input())


producer.send('foo', string.encode())

sleep(2)

# output
print(string)