import os 
import json

from resquests import Requests
from interfaces.Iapi import Iapi

class MovieSuggestionsProvider(Iapi):

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

        self.data['messages'][0]['content'] = f"Recommend {limit} movies for those who enjoy {NameMovie.upper()}." + "Returns only the movie names in JSON format, in the following structure: { movies: [movie1, movie2, ...]}"

        requestSuggestions = Requests(baseUrl=self.endpoint, params=json.dumps(self.data), headers=self.headers)
        MovieSuggestions = requestSuggestions.post()
        

        return MovieSuggestions