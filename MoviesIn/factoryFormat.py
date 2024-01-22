from typing import Type
from  interfaces.IJsonFormat import IJsonFormat
from interfaces.absFormat import absFormat


class FactoryFormat(absFormat):

    def create(self,  format: Type[IJsonFormat]) -> IJsonFormat:
        self.__format = format()

        return self.__format