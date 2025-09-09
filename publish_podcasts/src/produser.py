from configurations.kafka_configuration import produce, send_event
from logger.logger_to_elasic import Logger
from publish_podcasts.src.read_files import ReadFiles
from publish_podcasts.src.config import *

logger = Logger.get_logger()


class Manager:
    def __init__(self):
        logger.info("The muezzin started")
        self.files = ReadFiles(FILE_PATH).read_metadata_on_file()
        self.producer = produce()

    # Posting messages to Kafka by topic
    def publish_messages(self, topic: str):
        logger.info("start to publish")
        documents = self.files
        for document in documents:
            send_event(self.producer, topic, document)
        logger.info("finish to publish")
