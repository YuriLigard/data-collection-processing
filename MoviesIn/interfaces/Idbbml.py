from typing import Type
from .Iconndb import Iconndb
from abc import ABC, abstractmethod


class Idbml(ABC):

    @abstractmethod
    def __init__(self, conn: Type[Iconndb]) -> None:

        "- conn: Type[Iconndb] - Objeto de conexão com o banco"
    
        raise Exception ("Implemente o método construtor para manipulação do banco de dados")

    @abstractmethod
    def add(self, key: str, value: str) -> str:
        
        raise Exception ("Implemente um método para inserção no banco")

    @abstractmethod
    def get(self, key: str) -> str | None:
        raise Exception ("Implemente um método para obter dados no banco")
    