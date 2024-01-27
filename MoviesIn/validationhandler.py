import json
from interfaces.Ivalidationhandler import IvalidationHandler


class ValidationHandler(IvalidationHandler):

    def validMovieSuggestions(self, resp: object) -> bool:

        if resp.status_code == 200:
            movietitles  = json.loads(resp.text)
            try:
                movietitles = movietitles['choices'][0]['message']['content']
                movietitles = json.loads(movietitles)
                
                if isinstance(movietitles["movies"], list):
                    return True
            except json.decoder.JSONDecodeError as err:
                print(f"Erro: {err}")

                return False

    def validMovieInfo(self, respStreamingLink: object) -> bool:

        if respStreamingLink.status_code == 200:
            respStreamingLink = json.loads(respStreamingLink.text)  # erro
            if respStreamingLink['results'].get('BR'):
                
                return True
            
            
        return False
    
            


