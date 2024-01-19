from typing import Type
from .Iconndb import Iconndb
from abc import ABC, abstractmethod


class Idbml(ABC):
    

    def __init__(self, conn: Type[Iconndb]):
        raise Exception ("Impl...")


    def add(self) -> str:
        raise Exception ("Impl...")


    def search(self, search) -> str | None:
        raise Exception ("Impl...")
    