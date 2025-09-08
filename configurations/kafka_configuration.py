import json
from kafka import KafkaProducer
from kafka import KafkaConsumer
import os
from logger.logger_to_elasic import Logger

logger = Logger.get_logger()

kafka_broker = os.getenv('KAFKA_BROKER', 'localhost:9092')


def consumer(*topics):
    try:
        events = KafkaConsumer(*topics,
                               group_id='my_group',
                               value_deserializer=lambda m: json.loads(m.decode('ascii')),
                               bootstrap_servers=[kafka_broker],
                               auto_offset_reset='earliest'
                               )
        return events
    except Exception as e:
        logger.error(e)
        return


def produce():
    try:
        producer = KafkaProducer(bootstrap_servers=[kafka_broker],
                                 value_serializer=lambda x:
                                 json.dumps(x).encode('utf-8'))
        return producer
    except Exception as e:
        logger.error(e)
        return


def send_event(producer, topic, event):
    producer.send(topic, event)
    producer.flush()
