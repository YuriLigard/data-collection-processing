from typing import Type
from .IJsonFormat import IJsonFormat
from abc import ABC, abstractmethod


class absFormat(ABC):

    @abstractmethod
    def create(self, format: Type[IJsonFormat]) -> IJsonFormat:
        raise Exception("ddd")
