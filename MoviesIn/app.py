import os 
import json

from resquests_with_caching import RequestsWithCaching
from factoryDb import FactoryDb
from conndb import Conndb
from dbDml import DbDml

from contentP import ContentPrinting


class MovieSuggestionsProvide:

    def __init__(self) -> None:

        print ("Entrou no __init__")

        # Params API
        self.headers = dict()
        self.data = dict()

        self.endpoint = 'https://api.openai.com/v1/chat/completions'

        self.headers['Authorization'] = f'Bearer {os.environ.get("API_KEY_GPT")}'
        
        self.headers['Content-Type'] = 'application/json'

        self.data['model'] = "gpt-3.5-turbo"
        self.data['messages'] = [{'role': 'user', 'content':None}]

        # Creating DB 
        redis = FactoryDb()
        redis.createConn(Conndb)
        self.dbcache = redis.createDml(DbDml)

    

    def get(self, NameMovie, limit=5):

        params = dict()

        self.data['messages'][0]['content'] = 'suggest {0} films for those who like {1}. Returns only movie names in JSON format'.format(limit, NameMovie.upper())

        params["headers"] = self.headers
        params["data"] = json.dumps(self.data)

        request = RequestsWithCaching(self.endpoint, params, self.dbcache)
        resp = request.post()
        return ContentPrinting.get_MovieSuggestions(json.loads(resp))
        
    


if __name__ == '__main__':
    app = MovieSuggestionsProvide()

    cont = 0
    while cont <= 2:
        filme = input("nome filme: ")
        res = app.get(filme)
        print(res)
        cont+=1