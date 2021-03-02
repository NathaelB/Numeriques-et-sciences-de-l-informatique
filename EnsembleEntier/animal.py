from abc import ABC, abstractmethod


class Animal(ABC):

    @abstractmethod
    def __init__(self, race: str, genre: int):
        self._race: str = race
        self._genre: int = genre

    @abstractmethod
    def __str__(self):
        return f"je suis {self._race}"

    def verifReproduction(self, animal: 'Animal') -> bool:
        if self._race == animal._race and self._genre != animal._genre: return f"Ils peuvent se reproduire {self._race}"

    def communiquer(self):
        print("Je parle")

    @abstractmethod
    def je_mange(self):
        pass


class Canis(Animal):
    @abstractmethod
    def __init__(self, genre: int):
        super().__init__("canis", genre)
        self._repas = "Viande"

    def __str__(self):
        return f"je suis {self._race}"

    def communiquer(self):
        print("ouaf ouaf")

    def je_mange(self):
        print(f"Je mange de la {self._repas}")

class Chien(Canis):
    def __init__(self):
        super().__init__(0)

    def __str__(self):
        return "je suis un chien"
class Chienne(Canis):
    def __init__(self):
        super().__init__(1)

    def __str__(self):
        return "je suis une chienne"

class Bovin(Animal):
    @abstractmethod
    def __init__(self, genre: int):
        super().__init__("Bovin", genre)
        self._repas = "Thélio"

    def __str__(self):
        return f"je suis {self._race}"

    def je_mange(self):
        print(f"Je mange de la {self._repas}")

    def communiquer(self):
        print("meuh meuh")

class Taureau(Bovin):
    def __init__(self):
        super().__init__(0)

    def __str__(self):
        return "Je suis un vilain Taureau"
class Vache(Bovin):
    def __init__(self):
        super().__init__(1)
    def __str__(self):
        return "je suis une vache qui fait du lait MEUHHHH"


def main():
    a = Chien()
    b = Chienne()
    vache = Vache()
    taureau = Taureau()

    print(vache.verifReproduction(taureau))
    print(vache, taureau)
    print(a.verifReproduction(b))
    vache.je_mange()


if __name__ == '__main__':
    main()
