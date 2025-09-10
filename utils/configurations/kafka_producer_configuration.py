import json
from kafka import KafkaProducer
from utils.logger.logger_to_elasic import Logger
from utils.configurations.config import *

logger = Logger.get_logger()


class Producer:

    def __init__(self):

        try:
            self.producer = KafkaProducer(bootstrap_servers=[KAFKA_BROKER],
                                     value_serializer=lambda x:
                                     json.dumps(x).encode('utf-8'))

        except Exception as e:
            logger.error(f"Kafka producer connection error {e}")
            raise


    def send_event(self, topic, event):
        try:
            self.producer.send(topic, event)
            self.producer.flush()
            logger.info(f"The event: {event} send to topic: {topic}")

        except Exception as e:
            logger.error(f"The event failed to send {e}")
            raise