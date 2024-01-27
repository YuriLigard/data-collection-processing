from typing import Type
from .Iapi import Iapi
from abc import ABC, abstractmethod

class absAPI(ABC):

    @abstractmethod
    def create(self, RequestAPI: Type[Iapi]) -> Iapi:
        raise Exception("Instancie aqui")
    
