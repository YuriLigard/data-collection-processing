from abc import ABC, abstractmethod


class IJsonFormat(ABC):

    @abstractmethod
    def respGptFormat(self, key, resp: object) -> dict:
        raise Exception("impl...")
    
    @abstractmethod
    def respTmdbFormat(self, key, resp: object, resp1: object) -> dict:
        raise Exception("impl...")
    
    @abstractmethod
    def joinRespTmdbGpt(self, key, respGPT: dict, respTmdb: dict) -> dict:
        raise Exception("Imp....")