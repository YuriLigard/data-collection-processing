from typing import Type
from .Ivalidationhandler import IvalidationHandler
from abc import ABC, abstractmethod


class absValidation(ABC):

    @abstractmethod
    def create(self, validate: Type[IvalidationHandler]) -> IvalidationHandler:
        raise Exception("ddd")
