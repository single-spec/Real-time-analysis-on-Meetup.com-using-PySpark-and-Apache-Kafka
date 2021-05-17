#!/usr/bin/env python
#Created by Sonal Ingle

from kafka import KafkaConsumer
import json

# Subscribing a consumer to listen to topic1
meetup_consumer = KafkaConsumer('topic1', group_id = '1', bootstrap_servers = ['localhost:9092'])

# Printing the message
for message in meetup_consumer:
	print (type(message.value))
