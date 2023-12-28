from app import MovieSuggestionsProvide
from tmdb import MovieInfo


if __name__ == "__main__":

    ms = MovieSuggestionsProvide()
    listmovies = ms.get("O espaço entre nós")

    mi = MovieInfo()
    for movie in listmovies:
        print(movie)
        print(mi.get(movie))
