from typing import Type
from interfaces.Ivalidationhandler import IvalidationHandler
from interfaces.absValidation import absValidation


class FactoryValidation(absValidation):

    def create(self, validate: Type[IvalidationHandler]) -> IvalidationHandler:
        
        self.__validate = validate()
        return self.__validate
