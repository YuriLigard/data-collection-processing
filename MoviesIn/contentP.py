import json



class ContentPrinting:

    def get_MovieSuggestions(resp: dict):

        movietitles  = json.loads(resp['choices'][0]['message']['content'])

        return movietitles[list(movietitles.keys())[0]]



    def get_MovieInfo(resp: dict):
        
        movieInfo = resp["results"][0]
        return f"""
                Title: {movieInfo['original_title']}\n
                Avaliação: {movieInfo['vote_average']}\n
                História: {movieInfo['overview']}\n
                Link: {resp['link']}\n"""  #melhorar isso
                
    