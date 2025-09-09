import json
from kafka import KafkaProducer
from kafka import KafkaConsumer
import os
from logger.logger_to_elasic import Logger
from configurations.config import *

logger = Logger.get_logger()


def consumer(*topics):
    try:
        events = KafkaConsumer(*topics,
                               group_id='my_group',
                               value_deserializer=lambda m: json.loads(m.decode('ascii')),
                               bootstrap_servers=[KAFKA_BROKER],
                               auto_offset_reset='earliest'
                               )
        return events
    except Exception as e:
        logger.error(e)
        return


def produce():
    try:
        producer = KafkaProducer(bootstrap_servers=[KAFKA_BROKER],
                                 value_serializer=lambda x:
                                 json.dumps(x).encode('utf-8'))
        return producer
    except Exception as e:
        logger.error(e)
        return


def send_event(producer, topic, event):
    producer.send(topic, event)
    producer.flush()
    logger.info(f"The event: {event} send to topic: {topic}")
