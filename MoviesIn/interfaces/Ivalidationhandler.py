from typing import Type
from abc import ABC, abstractmethod


class IvalidationHandler(ABC):

    @abstractmethod
    def validMovieSuggestions(self, resp: object) -> bool:
        raise Exception("Implemente um método para validar se o JSON retornado pela API GPT atende a requisição feita")
        #https://platform.openai.com/docs/api-reference/making-requests
    
    @abstractmethod
    def validMovieInfo(self, resp: object) -> bool:
        raise Exception("Implemente um método para validar se o JSON retornado pela API TMDB atende a requisição feita")
        #https://developer.themoviedb.org/reference/intro/getting-started
