from abc import ABC, abstractmethod
from typing import List
from datetime import date


class Document(ABC):
    @abstractmethod
    def __init__(self, title: str):
        """
        "__init__" is a reseved method in python classes.
        It is called as a constructor in object oriented terminology.
        This method is called when an object is created from a class and
        it allows the class to initialize the attributes of the class.
        :param title:
        """

        self.documents = None
        self._title: str = title  # Titre du document
        self._emprunt: bool = False  # Information sur l'emprunt du document

    @abstractmethod
    def __str__(self):
        """
        This method returns the string representation of the object. This method
        is called when print() or str() function is invoked on an object.
        :return: Permet de nous renseigner sur le type du document (CD, LIVRE)
        """
        s = f"Mediatheque : {len(self.documents)} documents\n"
        s += f'{"index":^5}|{"document":^10}|{"titre":^26}|{"auteur/compositeur":^20}|{"interprete":^20}|{"disponible":^10}|\n'

    def getTitle(self) -> str:
        return self._title.capitalize()

    def setTitle(self, title: str):
        self._title = title

    def isEmprunt(self) -> bool:
        return self._emprunt == True

    def alertEmprunt(self):
        return self._emprunt == True

    def make(self):
        return self._emprunt == False


class CD(Document):
    def __init__(self, title: str, interpret: str, compositor: str):
        super().__init__(title)
        self._interpret = interpret
        self._compositor = compositor

    def __str__(self):
        return f"Le nom du cd: {self._title}\nL'interprète du cd: {self._interpret}\nLe compositeur du cd: {self._compositor}"

    def getCompositor(self):
        return self._compositor


class Livre(Document):
    def __init__(self, title: str, author: str):
        super().__init__(title)
        self._author = author

    def __str__(self):
        """
        Sizes itself to the table header
        so that each column is aligned
        :return:
        """
        return f"{'Livre':<10}|{self.getTitle():<26}|{self.getAuthor():<20}|{'':<20}|/n"

    def getAuthor(self):
        return self._author

    def addAuthor(self):
        pass

    def isEmprunt(self) -> 'Empruntlivre':
        self.alertEmprunt()
        return Empruntlivre()


class Mediatheque:
    def __init__(self):
        self._documents: List[Document] = []

    def __str__(self):
        """
        Create the top of the table with the
        title of each column and its spacing.
        :return:
        """
        s = f'{"index":^8}|{"document":^10}|{"titre":^26}|{"auteur/compositeur":^20}|{"interprete":^20}|{"disponible":^13}|\n'
        for i, d in enumerate(self._documents):
            s += f"{i:<8}|" + str(d)
        return s

    def add(self, d: 'Document'):
        """
        Add a document with the condition that if the document
        exists, the function will return an error.
        ---
        Putting under try to launch an error of the expiry case
        :param d:
        :return:
        """
        if self.search(d.getTitle()):
            return "Le document existe déjà"
        else:
            self._documents.append(d)

    def search(self, title: str) -> bool:
        """
        Allows you to search for a document
        :param doc:
        :return:
        """
        for i in range(len(self._documents)):
            if self._documents[i].getTitle() == title: return True
        return False

    # noinspection PyTypeChecker
    def searchCD(self, c: str) -> bool:
        """

        :param c: compositeur
        :return: Bool
        """
        for i in range(len(self._documents)):
            """
            On vérifie que le document est
            bien une instance de de CD
            """
            if isinstance(self._documents[i], CD):
                """
                On vérifie si le compositeur du document
                est bien celui recherché
                """
                cd: CD = self._documents[i]  # Permet ici de récupérer les méthodes de la class CD
                if cd.getCompositor() == c: return True

    def get_document(self):
        return self._documents




class Empruntlivre(object):
    pass


class Adherent(object):
    def emprunter(self, param):
        pass

    def terminer_emprunt(self, param):
        pass


def main():
    l = Livre("les misérables", "Victor Hugo")
    l2 = Livre("Choucroute", "Florien la pute")
    cd = CD("j'aime le code", "Nathaël Bonnal", "Thomas meyer")
    media = Mediatheque()

    media.add(l)
    media.add(l2)
    print(media)
    # d = Document("chapichapo") # L'erreur est normal, on bloque
    # print(d)

    # e = Empruntlivre(date.today(), l)
    # m = Mediatheque()
    # m.add(l)
    # m.add(Livre("Essais", "Montaigne"))
    # m.add(Livre("Le bois", "Jacques Dutronc"))
    # m.add(Livre("Le silence", "Thomas Meyer"))
    # m.add(Livre("Parler", "Nathaël Bonnal"))
    # m.add(Livre("Les boucles", "Kevin Terrison"))
    # m.add(Livre("Douceur du code", "Thélio Doucet"))
    # m.add(CD("j'aime le code", "Nathaël Bonnal", "Thomas meyer"))
    # m.add(CD("Quand j'étais petit codeur", "Thélio Doucet", "Thélio Doucet"))
    # m.add(CD("Le rap du codeur", "Kevin Terrison", "Thomas Meyer"))
    # m.add(CD("Silence on code", "Thomas Meyer", "Nathaël Bonnal"))
    # m.add(CD("print print print", "Nathaël Bonnal", "Thélio Doucet"))
    # print(m.search(m.get_document(8).get_titre()))
    # pierre = Adherent("Pierre")
    # pierre.emprunter(m.get_document(8))
    # print(pierre)
    # print(m)
    # pierre.emprunter(m.get_document(1))
    # pierre.emprunter(m.get_document(2))
    # pierre.emprunter(m.get_document(9))
    # pierre.emprunter(m.get_document(8))
    # pierre.emprunter(m.get_document(11))
    # pierre.emprunter(m.get_document(0))
    # print(pierre)
    # print(m)
    # pierre.terminer_emprunt(0)
    # print(pierre)
    # print(m)


if __name__ == '__main__':
    main()
