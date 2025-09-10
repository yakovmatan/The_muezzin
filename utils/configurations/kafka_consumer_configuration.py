import json
from kafka import KafkaConsumer
from utils.logger.logger_to_elasic import Logger
from utils.configurations.config import *

logger = Logger.get_logger()


class Consumer:

    def __init__(self, *topics):
            try:
                self.consumer = KafkaConsumer(*topics,
                                       group_id='my_group',
                                       value_deserializer=lambda m: json.loads(m.decode('ascii')),
                                       bootstrap_servers=[KAFKA_BROKER],
                                       auto_offset_reset='earliest'
                                       )

            except Exception as e:
                logger.error(e)
                return
