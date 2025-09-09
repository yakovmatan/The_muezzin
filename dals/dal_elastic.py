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

    # Insert documents to elastic
    def index_document(self, index_name: str, documents, doc_id):
        try:
            res = self.es.index(index=index_name, id=doc_id, document=documents)
            self.es.indices.refresh(index=index_name)
            logger.info(f"result={res['result']} the document insert to index: {index_name}")

        except Exception as e:
            logger.error(f"Failed to index document: {e}")

    # Update document in elastic with a new field
    def add_field(self, index_name: str, document_id, new_value: str, new_filed: str):
        try:
            update_data = {
                "doc": {
                    new_filed: new_value,
                }
            }

            response = self.es.update(index=index_name, id=document_id, body=update_data)
            self.es.indices.refresh(index=index_name)
            logger.info(f"Update response: {response}")

        except Exception as e:
            logger.error(f"Error updating document: {e}")

    def add_fields(self, index_name: str, document_id, **fields_and_value):
        try:
            update_data = {
                "doc": {
                    **fields_and_value,
                }
            }

            response = self.es.update(index=index_name, id=document_id, body=update_data)
            self.es.indices.refresh(index=index_name)
            logger.info(f"Update response: {response}")

        except Exception as e:
            logger.error(f"Error updating document: {e}")
