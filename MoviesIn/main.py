from conndb import Conndb
from dbDml import DbDml
from factoryDb import FactoryDb

from gpt import MovieSuggestionsProvide
from tmdb import MovieInfo
from factoryRequestAPI import FactoryRequestAPI

from validationhandler import ValidationHandler
from factoryValidation import FactoryValidation

from jsonFormat import JsonFormat
from factoryFormat import FactoryFormat


if __name__ == "__main__":

    #ms = MovieSuggestionsProvide()
    #listmovies = ms.get("Sohor dos Aneis")

    #mi = MovieInfo()
    #for movie in listmovies:
        #print(movie)
        #print(mi.get(movie))
    

    # Factory DB 
    factoryDb = FactoryDb()
    redisConn = factoryDb.createConn(Conndb)
    redisCache = factoryDb.createDml(DbDml)

    # Factorys API
    factoryAPI = FactoryRequestAPI()
    gptAPI = factoryAPI.create(MovieSuggestionsProvide)
    tmdbAPI = factoryAPI.create(MovieInfo)

    # Factory validadorJson 
    factoryValidation = FactoryValidation()
    validate = factoryValidation.create(ValidationHandler)

    # Factory ProcessadorJson
    factoryFormat = FactoryFormat()
    jsonFormat = factoryFormat.create(JsonFormat)

    #####

    key = "Os "  ###

    # if key in cache:

    # else: 
    respgpt = gptAPI.get(key)

    if respgpt:

        if validate.validMovieSuggestions(respgpt):
            MovieSuggestionsDict = jsonFormat.respGptFormat(key, respgpt)

            for nameMovie in MovieSuggestionsDict[key]:
                respSynopsis, respStreamingLink = tmdbAPI.get(nameMovie)
             
                if respSynopsis:
                    if validate.validMovieInfo(respStreamingLink):
                        resp = jsonFormat.respTmdbFormat(nameMovie, respSynopsis, respStreamingLink)
                    else:
                        resp = jsonFormat.respTmdbFormat(nameMovie, respSynopsis, None)
                
                    print(resp)

                else:
                    print("não ok")
        else:
            print("errooooo!")
    else:
        print("Uh")










    #respSynopsis, respStreamingLink = tmdbAPI.get("Interstelar")

    #print(respSynopsis, respStreamingLink)

    #print(jsonFormat.respTmdbFormat(respSynopsis, respStreamingLink))

    #resp = gptAPI.get("Kung Fu")

    #print(jsonFormat.respGptFormat(resp))

    #print("-------> ",respSynopsis, respStreamingLink)


    #print(validate.validMovieSuggestions(resp))

    #print(validate.validMovieInfo(respStreamingLink))

                                





   