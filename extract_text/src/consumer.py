from configurations.elastic_configuration import ElasticConn
from configurations.kafka_configuration import consumer
from configurations.mongodb_configuration import DbConnection
from extract_text.src.convert_bytes import ConvertBytes
from extract_text.src.text_extraction import TextExtraction
from logger.logger_to_elasic import Logger
from dals.dal_elastic import DalElastic
from dals.dal_mongo import DalMongo

logger = Logger.get_logger()


class Consumer:

    def __init__(self, *topics_sub, index_name: str, new_field='text'):
        self.new_field = new_field
        self.index_name = index_name
        self.topic_sub = topics_sub
        self.events = consumer(*topics_sub)
        self.mongo_conn = DbConnection()
        self.elastic_conn = ElasticConn().get_es()
        self.dal_mongo = DalMongo(self.mongo_conn)
        self.dal_elastic = DalElastic(self.elastic_conn)
        self.text_extract = TextExtraction()

    @staticmethod
    def extract_id_from_message(document, field='id'):
        if not document[field]:
            return ""
        return document[field]

    def __extract_text(self, unique_id):
        file_bytes = self.dal_mongo.get_file_by_id(unique_id)
        file_audio = ConvertBytes(file_bytes).convert_to_audio()
        text = self.text_extract.extract_text_from_a_file(file_audio)
        return text

    def consume_messages(self):
        logger.info(f"starting to consume from: {self.topic_sub}")
        for i, messages in enumerate(self.events, start=1):
            unique_id = Consumer.extract_id_from_message(messages.value)
            text = self.__extract_text(unique_id)
            # Update in Elasticsearch
            self.dal_elastic.add_field(self.index_name, unique_id, text, self.new_field)
