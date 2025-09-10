from utils.configurations.elastic_configuration import ElasticConn
from utils.dals.dal_elastic import DalElastic
from services.data_retrieval.src.builder_query import ElasticQueryBuilder


class Manager:

    def __init__(self):
        self.ec = ElasticConn().get_es()
        self.dal_elastic = DalElastic(self.ec)
        self.query_builder = ElasticQueryBuilder()

    def get_all_podcasts(self, index_name):
        query_body = self.query_builder.add_match_all().build()
        return self.dal_elastic.search_by_query(index_name, query_body)

    def get_is_bds_podcasts(self, index_name):
        query_body = self.query_builder.add_term('is_bds', True).build()
        return self.dal_elastic.search_by_query(index_name, query_body)
