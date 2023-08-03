from confluent_kafka import Producer
import re

class KafkaProducer:

    def __init__(self, bootstrap_server):
        self.bootstrap_server = bootstrap_server
        self.producer = Producer({'bootstrap.servers': self.bootstrap_server})


    def produce_mess(self, topic, message):
        self.producer.produce(topic, message)

    def flush(self):
        self.producer.flush()

    def produce_mess_with_keys(self, topic, message):
        #message_lowercase=message.lower()
        message_bytes = message.encode("utf-8")
        if  re.search("^[a-jA-J]",message) is not None:
            print('message starts with',"^[a-jA-J]")
            self.producer.produce(topic=topic, value=message_bytes,key="key0",partition=0 )
        if  re.search("^[k-oK-O]",message) is not None:
            self.producer.produce(topic=topic, value=message_bytes,key="key1",partition=1  )
            print('message starts with', "^[k-oK-O]")
        if  re.search("^[p-zP-Z]",message) is not None:
            self.producer.produce(topic=topic, value=message_bytes,key="key2",partition=2  )
            print('message starts with', "^[p-zP-Z]")
        # else:
        #     self.producer.produce(topic=topic, value=message_bytes, key="key0",partition=0 )
        #     print('message starts with', allkeys[0])
