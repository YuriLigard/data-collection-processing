from typing import Type

from interfaces.absDB import absDB
from interfaces.Iconndb import Iconndb
from interfaces.Idbbml import Idbml


class FactoryDb(absDB):


    def createConn(self, database: Type[Iconndb], db: int) -> Iconndb:

        self.__conn = database(db)
        self.__conn = self.__conn.connect()
        return self.__conn
    
   
    def createDml(self, databaseDml: Type[Idbml], conn: object) -> Idbml:

        self.__insert = databaseDml(conn)
        return self.__insert