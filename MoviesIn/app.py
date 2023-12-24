import json

from resquests_with_caching import RequestsWithCaching
from factoryDb import FactoryDb
from conndb import Conndb
from dbDml import DbDml


class Indica:

    def __init__(self, NamesMovie: list) -> None:
        self.endpoint = "https://api.openai.com/v1/chat/completions"
        self.NameMovie = NamesMovie
        self.limit = 5
        self.authorization = "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"
        self.ContentType = 'application/json'
        self.model = "gpt-3.5-turbo"
        self.messages = 'suggest 5 films for those who like Divergent. Returns only movie names in JSON format'

        redis = FactoryDb()
        
        redis.createConn(Conndb)
        self.dbcache = redis.createDml(DbDml)
        
    def get_movies_from_tastedive(self):
        params = dict()
        headers = dict()
        data = dict()

        headers['Content-Type']  = self.ContentType
        headers['Authorization'] = f'Bearer {self.authorization}'
        
        
        data['model'] = self.model
        data['messages'] = [{'role': 'user', 'content':f'{self.messages}'}]
        
        #params["q"] = self.NameMovie

        params["headers"] = headers
        params["data"] = json.dumps(data)

        #return params['data']
        request = RequestsWithCaching(self.endpoint, params, self.dbcache)
        resp = request.post()
        return json.loads(resp)
        
    


if __name__ == '__main__':
    app = Indica(["Gone Girl"])
    print(app.get_movies_from_tastedive())