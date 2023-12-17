import json

from resquests_with_caching import RequestsWithCaching
from factoryDb import FactoryDb
from conndb import Conndb
from dbDml import DbDml


class Indica:

    def __init__(self, NamesMovie: list) -> None:
        self.endpoint = "https://tastedive.com/api/similar"
        self.NameMovie = NamesMovie
        self.limit = 5
        self.type = 'movies'
        self.callback = 'JSONP'

        redis = FactoryDb()
        
        redis.createConn(Conndb)
        self.dbcache = redis.createDml(DbDml)

    def get_movies_from_tastedive(self):
        params = dict()
        params["q"] = self.NameMovie
        params["type"] = self.type
        params["limit"] = self.limit
        params["callback"] = self.callback
        request = RequestsWithCaching(self.endpoint, params, self.dbcache)
        resp = request.get()
        return json.loads(resp)
    


if __name__ == '__main__':
    app = Indica(["Gone Girl"])
    print(app.get_movies_from_tastedive())