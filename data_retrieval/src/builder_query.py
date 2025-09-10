class ElasticQueryBuilder:
    def __init__(self):
        self.must = []
        self.should = []
        self.must_not = []

    def add_match(self, field: str, value: str, clause: str = "must"):
        query = {"match": {field: value}}
        self._add_clause(clause, query)
        return self

    def add_match_phrase(self, field: str, value: str, clause: str = "must"):
        query = {"match_phrase": {field: value}}
        self._add_clause(clause, query)
        return self

    def add_term(self, field: str, value, clause: str = "must"):
        query = {"term": {field: value}}
        self._add_clause(clause, query)
        return self

    def add_range(self, field: str, gte=None, lte=None, clause: str = "must"):
        range_query = {}
        if gte is not None:
            range_query["gte"] = gte
        if lte is not None:
            range_query["lte"] = lte

        query = {"range": {field: range_query}}
        self._add_clause(clause, query)
        return self

    def add_exists(self, field: str, clause: str = "must"):
        query = {"exists": {"field": field}}
        self._add_clause(clause, query)
        return self

    def _add_clause(self, clause: str, query: dict):
        if clause == "must":
            self.must.append(query)
        elif clause == "should":
            self.should.append(query)
        elif clause == "must_not":
            self.must_not.append(query)
        else:
            raise ValueError(f"Unknown clause: {clause}")

    def build(self) -> dict:
        bool_query = {}
        if self.must:
            bool_query["must"] = self.must
        if self.should:
            bool_query["should"] = self.should
        if self.must_not:
            bool_query["must_not"] = self.must_not

        return {"query": {"bool":bool_query}}