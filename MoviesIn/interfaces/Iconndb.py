from abc import ABC, abstractmethod


class Iconndb(ABC):

    @abstractmethod
    def __init__(self) -> None:
        raise Exception("Implemente o método Construtor para a conexão com o banco de dados.")
    
    @abstractmethod
    def connect(self) -> object:
        raise Exception("Implementar um método para estabelecer uma conexão com o banco de dados.")
    
    @abstractmethod
    def close(self, conn) -> object:
        raise Exception("Implementar um método para fechar a conexão com o banco de dados.")


