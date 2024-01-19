from abc import ABC, abstractmethod


class IJsonFormat(ABC):

    @abstractmethod
    def __init__(self, key) -> None:
        self.__key = key

    @abstractmethod
    def respGptFormat(self, resp: object) -> dict:
        raise Exception("impl...")
    
    @abstractmethod
    def respTmdbFormat(self, resp: object) -> dict:
        raise Exception("impl...")
    
    @abstractmethod
    def joinRespTmdbGpt(self, respGPT: dict, respTmdb: dict) -> dict:
        raise Exception("Imp....")