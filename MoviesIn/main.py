#!/usr/bin/env python3

import sys

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

from contentP import Content

if __name__ == "__main__":

    #Factory DB 
    factoryDb = FactoryDb()
    redisConnGpt = factoryDb.createConn(Conndb, db=0)
    redisCacheGpt = factoryDb.createDml(DbDml, redisConnGpt)
    #
    redisConnTmdb = factoryDb.createConn(Conndb, db=1)
    redisCacheTmdb = factoryDb.createDml(DbDml, redisConnTmdb)


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

    content = Content() 
    ###########

    key = " ".join(sys.argv[1:])

    # if key in cache: #criar chache gpt e cache tmdb
  
    # else: 
    rCacheGpt = redisCacheGpt.search(key)
    if rCacheGpt:

        MovieSuggestionsList = rCacheGpt.split(">>")

        for nameMovie in MovieSuggestionsList:
            rCacheTmdb = redisCacheTmdb.search(nameMovie)
            content.printing(nameMovie, rCacheTmdb)

    else:
        
        respgpt = gptAPI.get(key)

        if respgpt != None:

            if validate.validMovieSuggestions(respgpt):
                MovieSuggestions = jsonFormat.respGptFormat(respgpt)
                #Salvar em Cache aqui
                redisCacheGpt.add(key, MovieSuggestions)
                
                MovieSuggestionsList = MovieSuggestions.split(">>")
                for nameMovie in MovieSuggestionsList:
                    print(nameMovie)
                    rCacheTmdb = redisCacheTmdb.search(nameMovie)
                    if rCacheTmdb:
                        content.printing(nameMovie, rCacheTmdb)
                    else:
                        respSynopsis, respStreamingLink = tmdbAPI.get(nameMovie)
             
                        if respSynopsis != None and respStreamingLink != None:
                            validRespStreamingLink = validate.validMovieInfo(respStreamingLink)
                            if validRespStreamingLink:
                                resp = jsonFormat.respTmdbFormat(respSynopsis, respStreamingLink)
                                content.printing(nameMovie, resp)
                                # Salvar Em cache aqui
                                redisCacheTmdb.add(nameMovie, str(resp))
                            else:
                                resp = jsonFormat.respTmdbFormat(respSynopsis, None)
                                content.printing(nameMovie, resp)
                                redisCacheTmdb.add(nameMovie, str(resp))
                                # Salvar Em cache aqui

                        elif respSynopsis != None and respSynopsis.json().get("status_message") != None:
                            print("error: ",respSynopsis.status_code)
                            print(respSynopsis.json().get("status_message"))
                            break
                        elif respSynopsis != None and respSynopsis.json().get("total_results") == 0:
                            print(nameMovie, ".....")
                            continue
                        else:
                            print(respSynopsis)
                            break

                    
            else:
                #"Erro code GPT"
                print("error: ",respgpt.text)
                #print(respgpt.json()["error"]["message"])

        else:
            print("Erro None GPT")
       





# ped
# Clean and Coment
# Link Sinb Corr

                                





   