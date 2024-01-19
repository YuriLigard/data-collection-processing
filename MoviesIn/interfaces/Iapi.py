from abc import ABC, abstractmethod


class Iapi(ABC):

    @abstractmethod
    def __init__(self) -> None:
        raise Exception("implement a method...")

    @abstractmethod
    def get(self) -> object | None:
        raise Exception("implement a method...")