import json

from interfaces.IJsonFormat import IJsonFormat


class JsonFormat(IJsonFormat):

    def respGptFormat(self, resp: object) -> dict:

        movietitles  = json.loads(resp.text)
        movietitles = json.loads(movietitles['choices'][0]['message']['content'])
        movietitles = movietitles[(list(movietitles.keys())[0])]

        return ">>".join(movietitles)
    

    def respTmdbFormat(self, resp: object, resp1: object) -> dict:
    
        movieSynopsis = json.loads(resp.text)
        movieSynopsis = movieSynopsis['results'][0].get('overview')

        if resp1:
            streamingLink = json.loads(resp1.text)
            streamingLink =  streamingLink['results']['BR']['link']
        else:
            streamingLink = "None"
        

        return ">>".join([movieSynopsis, streamingLink])
    

    def joinRespTmdbGpt(self, key, respGPT: dict, respTmdb: dict) -> dict:
        return super().joinRespTmdbGpt(respGPT, respTmdb)