from elasticsearch import Elasticsearch

class DalElastic:

    def __init__(self, connection: Elasticsearch):
        self.es = connection

    def create_index(self, index_name: str, mapping: dict):
        if not self.es.indices.exists(index=index_name):
            self.es.indices.create(index=index_name, mappings={
                "properties": mapping
            })
            print(f"Index {index_name} created successfully")
            self.es.indices.refresh(index=index_name)

        else:
            print(f"Index {index_name} already exists")


    def index_documents(self, index_name, documents, doc_id):
        try:
            res = self.es.index(index=index_name, id=doc_id, document=documents)
            print(f"result={res['result']}")
            self.es.indices.refresh(index=index_name)
        except Exception as e:
            print(f"Failed to bulk index documents: {e}")