import json
import os 

from conndb import Conndb
from dbDml import DbDml
from factoryDb import FactoryDb

from gpt import MovieSuggestionsProvide
from tmdb import MovieInfo
from factoryRequestAPI import FactoryRequestAPI

from validationhandler import ValidationHandler
from factoryValidation import FactoryValidation


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
    









    #respSynopsis, respStreamingLink = tmdbAPI.get(",.")

    #resp = gptAPI.get("Kung Fu")

    print("-------> ",respSynopsis, respStreamingLink)


    #print(validate.validMovieSuggestions(resp))

    #print(validate.validMovieInfo(respStreamingLink))
