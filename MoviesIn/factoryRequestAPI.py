from typing import Type
from interfaces.Iapi import Iapi
from interfaces.absAPI import absAPI

class FactoryRequestAPI(absAPI):

    def create(self, RequestAPI: Type[Iapi]) -> Iapi:

        self.__RequestAPI = RequestAPI()
        return self.__RequestAPI
    
