#from conndb import Conndb
#from dbDml import DbDml
#from factoryDb import FactoryDb

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
    #factoryDb = FactoryDb()
    #redisConn = factoryDb.createConn(Conndb)
    #redisCache = factoryDb.createDml(DbDml)

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

    # if key in cache: #criar chache gpt e cache tmdb

    # else: 
    respgpt = gptAPI.get(key)

    

    if respgpt != None:

        if validate.validMovieSuggestions(respgpt):
            MovieSuggestionsDict = jsonFormat.respGptFormat(key, respgpt)

            for nameMovie in MovieSuggestionsDict[key]:
                respSynopsis, respStreamingLink = tmdbAPI.get(nameMovie)
             
                if respSynopsis != None:
                    validRespSynopsis, validRespStreamingLink = validate.validMovieInfo(respSynopsis, respStreamingLink)
                    if validRespSynopsis and validRespStreamingLink:
                        resp = jsonFormat.respTmdbFormat(nameMovie, respSynopsis, respStreamingLink)
                        print(resp)
                    elif validRespSynopsis:
                        resp = jsonFormat.respTmdbFormat(nameMovie, respSynopsis, None)
                        print(resp)
                    else:
                        #"Erro code TMDB"
                        print("error: ",respSynopsis.status_code)
                        print(respSynopsis.json()["error"]["message"])
                else:
                    print("Erro None TMDB")
        else:
            #"Erro code GPT"
            print("error: ",respgpt.status_code)
            print(respgpt.json()["error"]["message"])

    else:
        print("Erro None GPT")
       









    #respSynopsis, respStreamingLink = tmdbAPI.get("Interstelar")

    #print(respSynopsis, respStreamingLink)

    #print(jsonFormat.respTmdbFormat(respSynopsis, respStreamingLink))

    #resp = gptAPI.get("Kung Fu")

    #print(jsonFormat.respGptFormat(resp))

    #print("-------> ",respSynopsis, respStreamingLink)


    #print(validate.validMovieSuggestions(resp))

    #print(validate.validMovieInfo(respStreamingLink))

                                





   