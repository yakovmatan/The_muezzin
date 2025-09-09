from classified.src.enricher import Enricher
from configurations.elastic_configuration import ElasticConn
from configurations.kafka_configuration import consumer, produce, send_event
from logger.logger_to_elasic import Logger
from dals.dal_elastic import DalElastic
from dals.dal_mongo import DalMongo

logger = Logger.get_logger()


class Consumer:

    def __init__(self, *topics_sub, topic_pub, index_name: str, new_field='text', list_hostile: list, list_less_hostile: list):
        self.list_hostile = list_hostile
        self.list_less_hostile = list_less_hostile
        self.new_field = new_field
        self.index_name = index_name
        self.topic_sub = topics_sub
        self.topic_pub = topic_pub
        self.events = consumer(*topics_sub)
        self.producer = produce()
        self.elastic_conn = ElasticConn().get_es()
        self.dal_elastic = DalElastic(self.elastic_conn)


    @staticmethod
    def extract_id_from_message(document, field='id'):
        if not document[field]:
            return ""
        return document[field]

    def fields_and_value_to_add(self, text):
        fields_and_value = {}
        score, word_count = Enricher.risk_score(text, self.list_hostile, self.list_less_hostile)
        bds_percent = Enricher.danger_percentages(len(text), score, word_count)
        fields_and_value['bds_percent'] = bds_percent
        is_bds = Enricher.is_bds(bds_percent)
        fields_and_value['is_bds'] = is_bds
        bds_threat_level = Enricher.risk_level(bds_percent)
        fields_and_value['bds_threat_level'] = bds_threat_level
        return fields_and_value



    def consume_messages(self):
        logger.info(f"starting to consume from: {self.topic_sub}")
        for  messages in self.events:
            # get id from kafka
            unique_id = Consumer.extract_id_from_message(messages.value)
            # Get file from Elasticsearch by id
            file = self.dal_elastic.get_document_by_id(self.index_name, unique_id)
            # Update in Elasticsearch
            self.dal_elastic.add_fields(self.index_name, unique_id, **self.fields_and_value_to_add(file['text']))
