from utils.configurations.elastic_configuration import ElasticConn
from utils.configurations.kafka_consumer_configuration import Consumer
from utils.configurations.mongodb_configuration import DbConnection
from services.text_handling.src.convert_bytes import ConvertBytes
from services.text_handling.src.decoder import Decoder
from services.text_handling.src.enricher import Enricher
from services.text_handling.src.text_extraction import TextExtraction
from utils.logger.logger_to_elasic import Logger
from utils.dals.dal_elastic import DalElastic
from utils.dals.dal_mongo import DalMongo
from services.text_handling.src.fiels import *

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
        self.list_hostile = Decoder(HOSTILE).decoded_from_base64().lower().split(',')
        self.list_less_hostile = Decoder(LESS_HOSTILE).decoded_from_base64().lower().split(',')

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
        score = Enricher.risk_score(text, self.list_hostile, self.list_less_hostile)
        bds_percent = Enricher.danger_percentages(len(text), score)
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