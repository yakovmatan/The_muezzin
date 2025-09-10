from configurations.elastic_configuration import ElasticConn
from configurations.kafka_consumer_configuration import Consumer
from configurations.kafka_producer_configuration import Producer
from configurations.mongodb_configuration import DbConnection
from logger.logger_to_elasic import Logger
from dals.dal_elastic import DalElastic
from dals.dal_mongo import DalMongo
from processing.src.unique_identifier import get_unique_identifier

logger = Logger.get_logger()


class ConsumerManager:

    def __init__(self, *topics_sub, topic_pub, index_name: str, file_field='path'):
        self.file_field = file_field
        self.index_name = index_name
        self.topic_pub = topic_pub
        self.events = Consumer(*topics_sub).consumer
        self.producer = Producer()
        self.mongo_conn = DbConnection()
        self.elastic_conn = ElasticConn().get_es()
        self.dal_mongo = DalMongo(self.mongo_conn)
        self.dal_elastic = DalElastic(self.elastic_conn)
        self.__create_index_to_elasitc(index_name)

    def __create_index_to_elasitc(self, index_name: str):
        self.dal_elastic.create_index(index_name)

    def __fit_document_to_elastic(self, document, new_field='text'):
        doc = {}
        for i in document:
            if i != self.file_field:
                doc[i] = document[i]

        return doc

    def consume_messages(self):
        logger.info("starting to consume")
        for i, messages in enumerate(self.events, start=1):
            unique_id = get_unique_identifier(messages.value, str(i))
            # Message splitting
            doc = self.__fit_document_to_elastic(messages.value)
            # Sending to Elastic
            self.dal_elastic.index_document(self.index_name, doc, unique_id)
            # Sending to mongo
            self.dal_mongo.insert_file(messages.value[self.file_field], unique_id)
            # Sending id to kafka
            self.producer.send_event(self.topic_pub, {'id': unique_id})
