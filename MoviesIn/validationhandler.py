import json

from interfaces.Ivalidationhandler import IvalidationHandler


class ValidationHandler(IvalidationHandler):


    def validMovieSuggestions(self, resp: object) -> bool:

        if resp.status_code == 200:
            movietitles  = json.loads(resp.text)
            movietitles = json.loads(movietitles['choices'][0]['message']['content'])
            
            if isinstance(movietitles[(list(movietitles.keys())[0])], list):
                return True
        
        return False

    def validMovieInfo(self, respStreamingLink: object) -> bool:

        #print(respStreamingLink.json())
        if respStreamingLink.status_code == 200:
            respStreamingLink = json.loads(respStreamingLink.text)  # erro
            if respStreamingLink['results'].get('BR'):
                
                return True
            
            
        return False
    
            


