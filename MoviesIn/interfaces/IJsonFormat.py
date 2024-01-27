from abc import ABC, abstractmethod


class IJsonFormat(ABC):

    @abstractmethod
    def respGptFormat(self, resp: object) -> str:
        raise Exception('''Implemente um método para extrair e formatar os nomes dos filmes retornados na API JSON GPT em uma única string, separada por ">>".
                           Caminho atual ['choices'][0]['message']['content'] -> ["f","f","f"...]
                        ''')
    
    @abstractmethod
    def respTmdbFormat(self, resp: object, resp1: object) -> str:
        raise Exception('''Implemente um método para extrair e formatar a sinopse e o link retornados na API JSON TMDB em uma única string, separada por ">>".
                            Caminho atual:
                              Sinopse: movieSynopsis['results'][0]['overview'] -> "tal tal....."
                              link: ['results']['BR']['link'] -> "https://www..."
                        ''')