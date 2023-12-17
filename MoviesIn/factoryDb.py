from conndb import Conndb
from dbDml import DbDml


class FactoryDb:


    def createConn(self, database: object) -> object:

        self.__conn = database()
        self.__conn = self.__conn.connect()
        return self.__conn
    
   
    def createDml(self, databaseDml: object) -> object:

        self.__insert = databaseDml(self.__conn)
        return self.__insert