from typing import Type
from abc import ABC, abstractmethod


class IvalidationHandler(ABC):

    @abstractmethod
    def validMovieSuggestions(self, resp: object) -> bool:
        raise Exception("Imp. metodo que valide o retorno")
    
    @abstractmethod
    def validMovieInfo(self, resp: object) -> bool:
        raise Exception("Imp. metodo que valide o retorno")
