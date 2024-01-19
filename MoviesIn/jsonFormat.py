import json

from interfaces.IJsonFormat import IJsonFormat


class JsonFormat(IJsonFormat):

    def __init__(self, key) -> None:
        self.__key = key

    def respGptFormat(self, resp: object) -> dict:

        movietitles = json.loads(resp['choices'][0]['message']['content'])
        movietitles = movietitles[(list(movietitles.keys())[0])] # melhorar 

        return movietitles

    def respTmdbFormat(self, resp: object, resp1: object) -> dict:
        pass


    

    def joinRespTmdbGpt(self, respGPT: dict, respTmdb: dict) -> dict:
        return super().joinRespTmdbGpt(respGPT, respTmdb)