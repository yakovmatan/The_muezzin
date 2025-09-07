from configurations.elastic_configuration import ElasticConn
from configurations.kafka_configuration import consumer, produce
from configurations.mongodb_configuration import DbConnection
from processing.src.dal_elastic import DalElastic
from processing.src.dal_mongo import DalMongo
from processing.src.unique_identifier import get_unique_identifier


class Consumer:

    def __init__(self, *topics, index_name):
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

    @staticmethod
    def fit_document_to_elastic(document):
        doc = {}
        for i in document:
            if i != "path":
                doc[i] = document[i]

        return doc


    def publish_messages(self):
        for i, messages in enumerate(self.events, start=1):
            unique_id = get_unique_identifier(messages.value, i)
            doc = Consumer.fit_document_to_elastic(messages.value)
            self.dal_elastic.index_documents(self.index_name, doc, unique_id)

            self.dal_mongo.insert_file(messages.value["path"], unique_id)
