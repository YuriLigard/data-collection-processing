#!/usr/bin/env python3
import sys

from conndb import Conndb
from dbDml import DbDml
from factoryDb import FactoryDb

from gpt import MovieSuggestionsProvider 
from tmdb import MovieInfo
from factoryRequestAPI import FactoryRequestAPI

from validationhandler import ValidationHandler
from factoryValidation import FactoryValidation

from jsonFormat import JsonFormat
from factoryFormat import FactoryFormat

from contentP import Content



if __name__ == "__main__":
    # Configuração da Factory do Banco de Dados

    # Cache no banco de dados (DB0) para nomes dos filmes sugeridos pelo GPT
    factoryDb = FactoryDb()
    redisConnGpt = factoryDb.createConn(Conndb, db=0)
    redisCacheGpt = factoryDb.createDml(DbDml, redisConnGpt)

    # Cache no banco de dados (DB1) para sinopses e links obtidos da API TMDB
    redisConnTmdb = factoryDb.createConn(Conndb, db=1)
    redisCacheTmdb = factoryDb.createDml(DbDml, redisConnTmdb)


    # Configuração da Factory das APIs

    factoryAPI = FactoryRequestAPI()

    # Instância da API GPT para sugestão de filmes
    gptAPI = factoryAPI.create(MovieSuggestionsProvider)

    # Instância da API TMDB para consultar informações dos filmes
    tmdbAPI = factoryAPI.create(MovieInfo)


    # Configuração da Factory do Validador JSON

    factoryValidation = FactoryValidation()

    # Instância responsável por validar os JSONs retornados pelas APIs GPT e TMDB
    validate = factoryValidation.create(ValidationHandler)


    # Configuração da Factory do Processador JSON

    factoryFormat = FactoryFormat()

    # Instância responsável por extrair e formatar as informações necessárias
    jsonFormat = factoryFormat.create(JsonFormat)

    #####

    # Impressão em tela
    content = Content()
    ###########

    # Argumento chave que será usado para gerar as sugestões
    key = " ".join(sys.argv[1:])

   
  # Verifica o cache GPT
rCacheGpt = redisCacheGpt.search(key)

if rCacheGpt:
    # Se encontrou no cache GPT, verifica no cache TMDB
    MovieSuggestionsList = rCacheGpt.split(">>")

    for nameMovie in MovieSuggestionsList:
        # Busca no cache TMDB
        rCacheTmdb = redisCacheTmdb.search(nameMovie)

        if rCacheTmdb:
            # Se encontrou no cache TMDB, imprime o conteúdo
            content.printing(nameMovie, rCacheTmdb)
        else:
            # Se não encontrou no cache TMDB, chama a API TMDB para obter sinopse e link do filme
            respSynopsis, respStreamingLink = tmdbAPI.get(nameMovie)

            # 1ª Validação: Verifica se a resposta da API é válida
            if respSynopsis is not None and respStreamingLink is not None:
                # 2ª Validação: Verifica se o conteúdo da resposta é válido
                validRespStreamingLink = validate.validMovieInfo(respStreamingLink)

                if validRespStreamingLink:
                    # Formata a resposta e a imprime
                    resp = jsonFormat.respTmdbFormat(respSynopsis, respStreamingLink)
                    content.printing(nameMovie, resp)
                    redisCacheTmdb.add(nameMovie, resp)
                else:
                    resp = jsonFormat.respTmdbFormat(respSynopsis, "None")
                    content.printing(nameMovie, resp)
                    redisCacheTmdb.add(nameMovie, resp)
            # Tratamento de erros específicos
                # Nota 0: A resposta da API TMDB, ao solicitar a sinopse de um filme, é crucial e determinante para a obtenção do link correspondente ao filme. 
            elif respSynopsis is not None and respSynopsis.json().get("status_message") is not None:
                print("error: ", respSynopsis.status_code)
                print(respSynopsis.json().get("status_message"))
                break
            # Caso: API TMDB não encontrou o filme 
            elif respSynopsis is not None and respSynopsis.json().get("total_results") == 0:
                print(f"\033[1mTítulo do Filme:\033[0m {nameMovie}")
                continue
            else:
                print(f"Não foi possível continuar: {respSynopsis}")
                break

# Não tem em cache GPT
else:
    respgpt = gptAPI.get(key)

    # 1ª Validação: Verifica se a resposta da API GPT é válida
    if respgpt is not None:
        # 2ª Validação: Verifica se o conteúdo da resposta é válido (Nomes dos filmes ["tal","tal2","tal3"])
        if validate.validMovieSuggestions(respgpt):
            # Formata a resposta e a armazena em cache GPT
            MovieSuggestions = jsonFormat.respGptFormat(respgpt)
            redisCacheGpt.add(key, MovieSuggestions)

            MovieSuggestionsList = MovieSuggestions.split(">>")

            for nameMovie in MovieSuggestionsList:
                rCacheTmdb = redisCacheTmdb.search(nameMovie)

                if rCacheTmdb:
                    content.printing(nameMovie, rCacheTmdb)
                else:
                    respSynopsis, respStreamingLink = tmdbAPI.get(nameMovie)

                    if respSynopsis is not None and respStreamingLink is not None:
                        validRespStreamingLink = validate.validMovieInfo(respStreamingLink)

                        if validRespStreamingLink:
                            resp = jsonFormat.respTmdbFormat(respSynopsis, respStreamingLink)
                            print(resp)
                            content.printing(nameMovie, resp)
                            redisCacheTmdb.add(nameMovie, resp)
                        else:
                            resp = jsonFormat.respTmdbFormat(respSynopsis, None)
                            content.printing(nameMovie, resp)
                            redisCacheTmdb.add(nameMovie, resp)
                    elif respSynopsis is not None and respSynopsis.json().get("status_message") is not None:
                        print("error: ", respSynopsis.status_code)
                        print(respSynopsis.json().get("status_message"))
                        break
                    elif respSynopsis is not None and respSynopsis.json().get("total_results") == 0:
                        print(nameMovie)
                        continue
                    else:
                        print(respSynopsis)
                        break
        else:
            print("error: ", respgpt.text)
    else:
        print("Não foi possível continuar")