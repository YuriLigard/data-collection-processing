import os 
import json

from resquests import Requests
from interfaces.Iapi import Iapi

class MovieSuggestionsProvide(Iapi):

    def __init__(self) -> None:

        # Params API
        self.headers = dict()
        self.data = dict()

        self.endpoint = 'https://api.openai.com/v1/chat/completions'

        self.headers['Authorization'] = f'Bearer {os.environ.get("API_KEY_GPT")}'
        
        self.headers['Content-Type'] = 'application/json'

        self.data['model'] = "gpt-3.5-turbo"
        self.data['messages'] = [{'role': 'user', 'content':None}]

    

    def get(self, NameMovie, limit=5):

        self.data['messages'][0]['content'] = 'suggest {0} films for those who like {1}. Returns only movie names in JSON format'.format(limit, NameMovie.upper())

        requestSuggestions = Requests(baseUrl=self.endpoint, params=json.dumps(self.data), headers=self.headers)
        MovieSuggestions = requestSuggestions.post()
        

        return MovieSuggestions
        
    


if __name__ == '__main__':
    app = MovieSuggestionsProvide()

    cont = 0
    while cont <= 2:
        filme = input("nome filme: ")
        res = app.get(filme)
        print(res)
        cont+=1