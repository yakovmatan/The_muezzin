from configurations.elastic_configuration import ElasticConn
from configurations.kafka_configuration import consumer
from configurations.mongodb_configuration import DbConnection
from logger.logger_to_elasic import Logger
from dals.dal_elastic import DalElastic
from dals.dal_mongo import DalMongo
from processing.src.unique_identifier import get_unique_identifier

logger = Logger.get_logger()


class Consumer:

    def __init__(self, *topics_sub, index_name: str, file_field='path'):
        self.file_field = file_field
        self.index_name = index_name
        self.topic_sub = topics_sub
        self.events = consumer(*topics_sub)
        self.mongo_conn = DbConnection()
        self.elastic_conn = ElasticConn().get_es()
        self.dal_mongo = DalMongo(self.mongo_conn)
        self.dal_elastic = DalElastic(self.elastic_conn)


    def __extract_id_from_message(self, document, field='id'):
        if not document[field]:
            return ""
        return document[field]

