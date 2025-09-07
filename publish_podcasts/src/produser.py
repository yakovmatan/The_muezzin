from configurations.kafka_configuration import produce, send_event
from publish_podcasts.src.read_files import ReadFiles


class Manager:
    def __init__(self):
        self.files = ReadFiles('C:/podcasts').read_metadata_on_file()
        self.producer = produce()


    def publish_messages(self, topic):
        documents = self.files
        for document in documents:
            send_event(self.producer,topic , document)
