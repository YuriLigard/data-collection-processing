from abc import ABC, abstractmethod


class Iconndb(ABC):

    @abstractmethod
    def __init__(self) -> None:
        raise Exception("Impl....")
    
    @abstractmethod
    def connect(self) -> object:
        raise Exception("Impl....")
    
    @abstractmethod
    def close(self, conn) -> object:
        raise Exception("Impl....")


