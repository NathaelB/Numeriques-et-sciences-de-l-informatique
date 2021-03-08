from abc import ABC, abstractmethod


class Player(ABC):
    @abstractmethod
    def __init__(self, name: str, age: int):
        self._name = name
        self._age = age
        self._dump: bool = False

    @abstractmethod
    def __str__(self):
        pass

    def getName(self) -> str:
        return self._name.capitalize()

    def setName(self, name: str):
        self._name = name

    def isSilly(self) -> bool:
        return self._dump == True

    def alertSilly(self):
        return self._dump == True

    def make(self):
        return self._dump == False