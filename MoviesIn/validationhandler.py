import json

from interfaces.Ivalidationhandler import IvalidationHandler


class ValidationHandler(IvalidationHandler):


    def validMovieSuggestions(self, resp: object) -> bool:
        
        movietitles  = json.loads(resp.text)

        movietitles = json.loads(movietitles['choices'][0]['message']['content'])
    
        if isinstance(movietitles[(list(movietitles.keys())[0])], list):
            
            return True
        

        return False

    def validMovieInfo(self, respStreamingLink: object) -> bool:

        if respStreamingLink:
            respStreamingLink = json.loads(respStreamingLink.text)
            
            if respStreamingLink.get('results'):
                return True
        
        return False
            


