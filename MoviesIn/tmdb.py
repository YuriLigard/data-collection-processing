import os 
import json

from resquests_with_caching import RequestsWithCaching
from factoryDb import FactoryDb
from conndb import Conndb
from dbDml import DbDml

from contentP import ContentPrinting


class MovieInfo:

    def __init__(self) -> None:

        print ("Entrou no __init__")

        # Params API
        self.headers = dict()
        self.params = dict()

        self.endpoint = 'https://api.themoviedb.org/3/search/movie?'

        self.headers['Authorization'] = f'Bearer {os.environ.get("API_TOKEN_TMDB")}'
        self.headers['accept'] = 'application/json'

        self.params['page'] = 1
        self.params['include_adult'] = False


        # Creating DB 
        redis = FactoryDb()
        redis.createConn(Conndb)
        self.dbcache = redis.createDml(DbDml)

    

    def get(self, NameMovie, language='pt-BR'):

        self.params["headers"] = self.headers
        self.params["query"] = NameMovie
        self.params['language'] = language
        #print("***",self.params)
        #print("***",self.headers['Authorization'])

        request = RequestsWithCaching(self.endpoint, self.params, self.dbcache)
        resp = request.get() # Mudar só os paramns
        
        resp = json.loads(resp)
        url = f"https://api.themoviedb.org/3/movie/{resp['results'][0]['id']}/watch/providers"

        request2= RequestsWithCaching(url, self.params, self.dbcache)
        resp2 = request2.get() # Mudar só os paramns
        resp2 = json.loads(resp2)
        resp['link'] = resp2['results']['BR']['link']
        return ContentPrinting.get_MovieInfo(resp)
    


if __name__ == '__main__':
    app = MovieInfo()

    #filme = input("nome filme: ")
    res = app.get("Kung Fu")
    print(res)