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

    def index_documents(self, index_name: str, documents, doc_id):
        try:
            res = self.es.index(index=index_name, id=doc_id, document=documents)
            self.es.indices.refresh(index=index_name)
            logger.info(f"result={res['result']}")

        except Exception as e:
            logger.error(f"Failed to index document: {e}")

    def get_all_id_from_index(self, index_name: str):
        try:
            documents = self.es.search(index=index_name, body={
                "query": {"match_all": {}}
            }, size=10000)
            ls = []
            for hit in documents["hits"]["hits"]:
                doc_id = hit["_id"]
                ls.append(doc_id)
            logger.info("pull from elastic all id file")
        except Exception as e:
            logger.error(f"Failed to pulling id from elastic: {e}")

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
