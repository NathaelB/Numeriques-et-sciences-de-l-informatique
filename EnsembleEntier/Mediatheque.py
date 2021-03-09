from abc import ABC, abstractmethod
from typing import List, Union
from datetime import date, timedelta


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

    def getEmprunt(self):
        if self._emprunt == False:
            return f"Non"
        else:
            return f"Oui"

    def isEmprunt(self) -> bool:  # emprunte le doc
        return self._emprunt == True

    def alertEmprunt(self):  # nous signale si il est alerté
        return self._emprunt == True

    def giveBack(self):
        return self._emprunt == False


class CD(Document):
    def __init__(self, title: str, interpret: str, compositor: str):
        super().__init__(title)
        self._interpret = interpret
        self._compositor = compositor

    def __str__(self):

        return f"\n{'':^8}|{'CD':<10}|{self.getTitle():<26}|{self._compositor:<20}|{'':<20}|{self._interpret: <20}"

    def getCompositor(self):
        return self._compositor

    def setCompositor(self, compositor: str):
        self._compositor = compositor

    def getInterprete(self):
        return self._interpret

    def setInterprete(self, interprete: str):
        self._interpret = interprete


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
        return f"{'Livre':<10}|{self.getTitle():<26}|{self.getAuthor():<20}|{'':<20}|\n"

    def getAuthor(self):
        return self._author

    def setAuthor(self, author: str):
        self._author = author

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

    def getDocument(self, index: int) -> Union[Document, str]:
        try:
            return self._documents[index]
        except:
            return f"L'index '{index}' est hors plage"


class Emprunt(ABC):
    @abstractmethod
    def __init__(self, dateEmprunt: date, doc: Document, nbDayMake: int):
        self._doc = doc
        self._nbDayMake = nbDayMake
        self._dateEmprunt = dateEmprunt

    def __str__(self):
        s = f"|{'Document':^10}|{'Titre':^26}|{'Auteur':^20}|{' ':<20}|{'Disponibilité':<15}|{'Date':<15}|\n"
        s += f"{self._doc.__str__():^81}{self._doc.getEmprunt():^15}|{self._dateEmprunt}|"
        return s

    def isLate(self) -> bool:
        return (date.today() - self._dateEmprunt).days <= self._nbDayMake

    def empruntTerminate(self) -> 'Document':
        self._doc.giveBack()
        return self._doc

    def getDoc(self) -> 'Document':
        return self._doc


class Empruntlivre(Emprunt):
    def __init__(self, doc: Livre):
        super().__init__(date.today(), doc, 10)


class EmpruntCD(Emprunt):
    def __init__(self, doc: CD):
        super().__init__(date.today(), doc, 15)


class Adherent:
    def __init__(self, name: str):
        self._name = name
        self._borrowingInProgress: List[Emprunt] = []

    def isLate(self) -> bool:
        for emprunt in self._borrowingInProgress:
            if emprunt.isLate():
                return True
        return False

    def borrowingTrue(self) -> bool:
        return not self.isLate() and len(self._borrowingInProgress) < 5

    def emprunter(self, doc: Document):
        if self._borrowingInProgress is True:
            if isinstance(doc, Livre):
                self._borrowingInProgress.append(Empruntlivre(doc))
            if isinstance(doc, CD):
                self._borrowingInProgress.append(EmpruntCD(doc))
        else:
            print("Tu ne peux pas wesh :p")


    def terminer_emprunt(self, index: int):
        try:
            self._borrowingInProgress[index].empruntTerminate()
            self._borrowingInProgress.pop(index)
        except:
            return False



def main():
    l = Livre("les misérables", "Victor Hugo")
    l2 = Livre("Choucroute", "Florien la pute")
    cd = CD("j'aime le code", "Nathaël Bonnal", "Thomas meyer")
    media = Mediatheque()

    media.add(l)
    media.add(l2)
    print(media)


    m = Mediatheque()
    m.add(l)
    m.add(Livre("Essais", "Montaigne"))
    m.add(Livre("Le bois", "Jacques Dutronc"))
    m.add(Livre("Le silence", "Thomas Meyer"))
    m.add(Livre("Parler", "Nathaël Bonnal"))
    m.add(Livre("Les boucles", "Kevin Terrison"))
    m.add(Livre("Douceur du code", "Thélio Doucet"))
    m.add(CD("j'aime le code", "Nathaël Bonnal", "Thomas meyer"))
    m.add(CD("Quand j'étais petit codeur", "Thélio Doucet", "Thélio Doucet"))
    m.add(CD("Le rap du codeur", "Kevin Terrison", "Thomas Meyer"))
    m.add(CD("Silence on code", "Thomas Meyer", "Nathaël Bonnal"))
    m.add(CD("print print print", "Nathaël Bonnal", "Thélio Doucet"))
    print(m.search(m.getDocument(8).getTitle()))
    pierre = Adherent("Pierre")
    pierre.emprunter(m.getDocument(8))
    print(pierre)
    print(m)
    pierre.emprunter(m.getDocument(1))
    pierre.emprunter(m.getDocument(2))
    pierre.emprunter(m.getDocument(9))
    pierre.emprunter(m.getDocument(8))
    pierre.emprunter(m.getDocument(11))
    pierre.emprunter(m.getDocument(5))
    print(pierre)
    print(m)
    pierre.terminer_emprunt(0)
    print(pierre)
    print(m)


if __name__ == '__main__':
    main()
