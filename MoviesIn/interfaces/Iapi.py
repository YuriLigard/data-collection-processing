from abc import ABC, abstractmethod


class Iapi(ABC):

    @abstractmethod
    def __init__(self) -> None:
        raise Exception("Implemente o método construtor para API")
        # Params API
        # [GPT] https://platform.openai.com/docs/api-reference/introduction
        # [TMDB] https://developer.themoviedb.org/reference/intro/getting-started


    @abstractmethod
    def get(self) -> object | None:
        raise Exception("Implemente um método para executar o prompt")