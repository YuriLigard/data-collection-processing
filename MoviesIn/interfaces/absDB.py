from typing import Type
from .Iconndb import Iconndb
from .Idbbml import Idbml
from abc import ABC, abstractmethod


class absDB(ABC):

    @abstractmethod
    def createConn(self, database: Type[Iconndb]) -> Iconndb:
        raise Exception("Instancie aqui")
    
    @abstractmethod
    def createDml(self, databaseDml: Type[Idbml]) -> Idbml:
        raise Exception("Instancie aqui")