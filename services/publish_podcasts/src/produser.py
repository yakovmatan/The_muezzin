from utils.configurations.kafka_producer_configuration import Producer
from utils.logger.logger_to_elasic import Logger
from services.publish_podcasts.src.read_files import ReadFiles
from services.publish_podcasts.src.config import *

logger = Logger.get_logger()


class Manager:
    def __init__(self):
        logger.info("The muezzin started")
        self.files = ReadFiles(FILE_PATH).read_metadata_on_file()
        self.producer = Producer()

    # Posting messages to Kafka by topic
    def publish_messages(self, topic: str):
        logger.info("start to publish")
        documents = self.files
        for document in documents:
            self.producer.send_event(topic, document)
        logger.info("finish to publish")
