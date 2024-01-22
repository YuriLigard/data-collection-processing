import os 
from resquests import Requests
from interfaces.Iapi import Iapi

class MovieInfo(Iapi):

    def __init__(self) -> None:

        self.headers = dict()
        self.params = dict()

        self.endpoint = 'https://api.themoviedb.org/3/search/movie?'

        self.headers['Authorization'] = f'Bearer {os.environ.get("API_TOKEN_TMDB")}'
        self.headers['accept'] = 'application/json'

        self.params['page'] = 1
        self.params['include_adult'] = False
        

    def get(self, NameMovie, language='pt-BR'):

        self.params["query"] = NameMovie
        self.params['language'] = language

    
        requestSynopsis = Requests(baseUrl=self.endpoint, params=self.params, headers=self.headers)
        movieSynopsis = requestSynopsis.get() 

        if movieSynopsis.json()["total_results"] > 0:
            url = f"https://api.themoviedb.org/3/movie/{movieSynopsis.json()['results'][0]['id']}/watch/providers"
            # 322 pra simular um erro, correto é 3t
            requestStreaming = Requests(baseUrl=url, params=self.params, headers=self.headers)  
            streamingLink = requestStreaming.get()

            return movieSynopsis, streamingLink


        return None, None
    

    

if __name__ == '__main__':
    app = MovieInfo()

    #filme = input("nome filme: ")
    print(app.get("Kung Fu"))
  