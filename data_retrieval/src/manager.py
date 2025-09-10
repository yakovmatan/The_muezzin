from configurations.elastic_configuration import ElasticConn
from dals.dal_elastic import DalElastic

class Manager:

    def __init__(self):
        self.ec = ElasticConn().get_es()
        self.dal_elastic = DalElastic(self.ec)

    def get_all_podcasts(self, index_name):
        return self.dal_elastic.search_all(index_name)

