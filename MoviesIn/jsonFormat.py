import json

from interfaces.IJsonFormat import IJsonFormat


class JsonFormat(IJsonFormat):

    def respGptFormat(self, resp: object) -> str:

        movietitles  = json.loads(resp.text)
        movietitles = movietitles['choices'][0]['message']['content']
        movietitles = json.loads(movietitles)

        return ">>".join(movietitles["movies"])
    

    def respTmdbFormat(self, resp: object, resp1: object) -> str:
    
        movieSynopsis = json.loads(resp.text)
        movieSynopsis = movieSynopsis['results'][0].get('overview')

        if resp1:
            streamingLink = json.loads(resp1.text)
            streamingLink =  streamingLink['results']['BR']['link']
        else:
            streamingLink = "None"
        
        return ">>".join([movieSynopsis, streamingLink])