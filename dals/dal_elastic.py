from elasticsearch import Elasticsearch
from logger.logger_to_elasic import Logger

logger = Logger.get_logger()

class DalElastic:

    def __init__(self, connection: Elasticsearch):
        self.es = connection

    def create_index(self, index_name: str):
        if not self.es.indices.exists(index=index_name):
            self.es.indices.create(index=index_name)
            logger.info(f"Index {index_name} created successfully")
            self.es.indices.refresh(index=index_name)

        else:
            logger.info(f"Index {index_name} already exists")


    def index_documents(self, index_name, documents, doc_id):
        try:
            res = self.es.index(index=index_name, id=doc_id, document=documents)
            logger.info(f"result={res['result']}")
            self.es.indices.refresh(index=index_name)
        except Exception as e:
            logger.error(f"Failed to index document: {e}")
