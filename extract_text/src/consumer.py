from configurations.elastic_configuration import ElasticConn
from configurations.kafka_consumer_configuration import Consumer
from configurations.mongodb_configuration import DbConnection
from extract_text.src.convert_bytes import ConvertBytes
from extract_text.src.decoder import Decoder
from extract_text.src.enricher import Enricher
from extract_text.src.text_extraction import TextExtraction
from logger.logger_to_elasic import Logger
from dals.dal_elastic import DalElastic
from dals.dal_mongo import DalMongo
from extract_text.src.fiels import *

logger = Logger.get_logger()


class ConsumerManager:

    def __init__(self, *topics_sub, index_name: str):
        self.index_name = index_name
        self.topic_sub = topics_sub
        self.events = Consumer(*topics_sub).consumer
        self.mongo_conn = DbConnection()
        self.elastic_conn = ElasticConn().get_es()
        self.dal_mongo = DalMongo(self.mongo_conn)
        self.dal_elastic = DalElastic(self.elastic_conn)
        self.text_extract = TextExtraction()
        self.list_hostile = Decoder(HOSTILE).decoded_from_base64().split(',')
        self.list_less_hostile = Decoder(LESS_HOSTILE).decoded_from_base64().split(',')

    @staticmethod
    def extract_id_from_message(document, field='id'):
        if not document[field]:
            return ""
        return document[field]

    # Pull file bytes by id from mongo, convert the file bytes to file audio, Transcriber
    def __extract_text(self, unique_id):
        file_bytes = self.dal_mongo.get_file_by_id(unique_id)
        file_audio = ConvertBytes(file_bytes).convert_to_audio()
        text = self.text_extract.extract_text_from_a_file(file_audio)
        return text

    def __fields_and_value_to_add(self, text):
        fields_and_value = {'text': text}
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
            unique_id = ConsumerManager.extract_id_from_message(messages.value)
            # Extract text
            text = self.__extract_text(unique_id)
            # Update in Elasticsearch
            self.dal_elastic.add_fields(self.index_name, unique_id, **self.__fields_and_value_to_add(text))
