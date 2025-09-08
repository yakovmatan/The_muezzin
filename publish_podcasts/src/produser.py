from configurations.kafka_configuration import produce, send_event
from logger.logger import get_logger
from publish_podcasts.src.read_files import ReadFiles
from publish_podcasts.src.config import *

log = get_logger()


class Manager:
    def __init__(self):
        self.files = ReadFiles(FILE_PATH).read_metadata_on_file()
        self.producer = produce()

    #Posting messages to Kafka by topic
    def publish_messages(self, topic):
        log.info("start to publish")
        documents = self.files
        for document in documents:
            send_event(self.producer,topic , document)
        log.info("finish to publish")