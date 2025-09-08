from configurations.elastic_configuration import ElasticConn
from configurations.kafka_configuration import consumer, produce
from configurations.mongodb_configuration import DbConnection
from logger.logger import get_logger
from processing.src.dal_elastic import DalElastic
from processing.src.dal_mongo import DalMongo
from processing.src.unique_identifier import get_unique_identifier

log = get_logger()

class Consumer:

    def __init__(self, *topics, index_name, file_field='path'):
        self.file_field = file_field
        self.index_name = index_name
        self.events = consumer(*topics)
        self.producer = produce()
        self.mongo_conn = DbConnection()
        self.elastic_conn = ElasticConn().get_es()
        self.dal_mongo = DalMongo(self.mongo_conn)
        self.dal_elastic = DalElastic(self.elastic_conn)
        self.__create_index_to_elasitc(index_name)

    def __create_index_to_elasitc(self, index_name):
        self.dal_elastic.create_index(index_name)


    def __fit_document_to_elastic(self, document):
        doc = {}
        for i in document:
            if i != self.file_field:
                doc[i] = document[i]

        return doc


    def publish_messages(self):
        for i, messages in enumerate(self.events, start=1):
            log.info("starting to consume")
            unique_id = get_unique_identifier(messages.value, str(i))
            # Message splitting
            doc = self.__fit_document_to_elastic(messages.value)
            # Sending to Elastic
            self.dal_elastic.index_documents(self.index_name, doc, unique_id)
            # Sending to mongo
            self.dal_mongo.insert_file(messages.value[self.file_field], unique_id)

