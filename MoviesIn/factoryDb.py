from typing import Type

from interfaces.absDB import absDB
from interfaces.Iconndb import Iconndb
from interfaces.Idbbml import Idbml


class FactoryDb(absDB):


    def createConn(self, database: Type[Iconndb]) -> Iconndb:

        self.__conn = database()
        self.__conn = self.__conn.connect()
        return self.__conn
    
   
    def createDml(self, databaseDml: Type[Idbml]) -> Idbml:

        self.__insert = databaseDml(self.__conn)
        return self.__insert