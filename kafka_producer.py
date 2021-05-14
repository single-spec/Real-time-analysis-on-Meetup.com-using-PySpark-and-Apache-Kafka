from kafka import KafkaClient, KafkaProducer
import json,requests

kafka = KafkaClient(bootstrap_servers='localhost:9092')
#producer = KafkaProducer(bootstrap_servers='localhost:9092')

producer = KafkaProducer(kafka)

r = requests.get("https://stream.meetup.com/2/rsvps",stream=True)

for line in r.iter_lines():
	producer.send_messages('meetup',line)
	print(type(line))

kafka.close()