import json

from resquests_with_caching import RequestsWithCaching
from factoryDb import FactoryDb
from conndb import Conndb
from dbDml import DbDml


class Indica:

    def __init__(self, term: list) -> None:
        self.endpoint = " https://itunes.apple.com/search"
        self.term = term
        redis = FactoryDb()
        
        redis.createConn(Conndb)
        self.dbcache = redis.createDml(DbDml)

    def get_movies_from_tastedive(self):
        params = dict()
        params["term"] = self.term
        request = RequestsWithCaching(self.endpoint, params, self.dbcache)
        resp = request.get()
        return resp
    


if __name__ == '__main__':
    app = Indica(["Loucos por Jesus"])
    print(app.get_movies_from_tastedive()['results'][0])