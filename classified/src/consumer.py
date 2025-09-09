from configurations.elastic_configuration import ElasticConn
from configurations.kafka_configuration import consumer, produce, send_event
from extract_text.src.text_extraction import TextExtraction
from logger.logger_to_elasic import Logger
from dals.dal_elastic import DalElastic
from dals.dal_mongo import DalMongo

logger = Logger.get_logger()


class Consumer:

    def __init__(self, *topics_sub, topic_pub, index_name: str, new_field='text'):
        self.new_field = new_field
        self.index_name = index_name
        self.topic_sub = topics_sub
        self.topic_pub = topic_pub
        self.events = consumer(*topics_sub)
        self.producer = produce()
        self.elastic_conn = ElasticConn().get_es()
        self.dal_elastic = DalElastic(self.elastic_conn)
        self.text_extract = TextExtraction()

    @staticmethod
    def extract_id_from_message(document, field='id'):
        if not document[field]:
            return ""
        return document[field]


    def consume_messages(self):
        logger.info(f"starting to consume from: {self.topic_sub}")
        for  messages in self.events:
            # get id from kafka
            unique_id = Consumer.extract_id_from_message(messages.value)
            # Update in Elasticsearch
            self.dal_elastic.add_field(self.index_name, unique_id, text, self.new_field)
            # sending to kafka in
            send_event(self.producer, self.topic_pub, {'id': unique_id})
