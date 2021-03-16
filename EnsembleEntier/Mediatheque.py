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
        """
        Récupère le titre du document
        avec comme sa première lettre en majuscules
        """
        return self._title.capitalize()

    def setTitle(self, title: str):
        """
        Définis le titre d'un document
        :param title:
        :return:
        """
        self._title = title


    def isEmprunt(self):
        return self._emprunt

    def setEmprunt(self):
        """
        Définis que le document est
        emprunté
        :return:
        """
        self._emprunt = True

    def giveBack(self):
        """
        Redonne le document
        :return:
        """
        return self._emprunt == False

    def getEmprunt(self):
        """
        Méthode permettant
        de nous informer si tel document est
        disponible oui ou non
        :return:
        """
        if not self.isEmprunt():
            return f"Oui"
        else:
            return f"Non"

    @abstractmethod
    def emprunter(self):
        """
        Décoratrice pour pour la
        méthode emprunt dans Adhérent
        """
        pass


class CD(Document):
    def __init__(self, title: str, interpret: str, compositor: str):
        super().__init__(title)
        self._interpret = interpret
        self._compositor = compositor

    def __str__(self):

        return f"{'CD':^10}|{self.getTitle():^26}|{self._compositor:^20}|{self._interpret: ^20}|{self.getEmprunt():^13}|\n"

    def getCompositor(self):
        """
        Récupère le Compositeur
        :return:
        """
        return self._compositor

    def setCompositor(self, compositor: str):
        """
        Définis le Compositeur
        :param compositor:
        :return:
        """
        self._compositor = compositor

    def getInterprete(self):
        """
        Récupère l'interprete
        :return:
        """
        return self._interpret

    def setInterprete(self, interprete: str):
        """
        Définis l'Interprète
        :param interprete:
        :return:
        """
        self._interpret = interprete

    def emprunter(self) -> 'EmpruntCD':
        self.setEmprunt()
        return EmpruntCD(self)


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
        return f"{'Livre':^10}|{self.getTitle():^26}|{self.getAuthor():^20}|{'':<20}|{self.getEmprunt():^13}|\n"

    def getAuthor(self):
        return self._author

    def setAuthor(self, author: str):
        """
        Détermine l'auteur sur
        un document
        :param author:
        :return:
        """
        self._author = author

    def emprunter(self) -> 'Empruntlivre':
        self.setEmprunt()
        return Empruntlivre(self)


class Mediatheque:
    def __init__(self):
        self._documents: List[Document] = []

    def __str__(self):
        """
        Create the top of the table with the
        title of each column and its spacing.
        :return:
        """
        s = '/------------------------------------------------------------------------------------------------------\ \n'
        s += f'|{"index":^8}|{"document":^10}|{"titre":^26}|{"auteur/compositeur":^20}|{"interprete":^20}|{"disponible":^13}|\n'
        s += '|------------------------------------------------------------------------------------------------------|\n'
        for i, d in enumerate(self._documents):
            s += f"|{i:<8}|" + str(d)
        s +="\------------------------------------------------------------------------------------------------------/"
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
        :param title:
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
        """
        Permet de récupérer le document via un
        index

        Il return soit un Document si il trouve via l'index
        soit une erreur programmé grâce au try & except
        :param index:
        :return:
        """
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
        s = f"{self._doc.__str__()[:80]:^80}{str(self._dateEmprunt):^15}|{str(timedelta(days= self._nbDayMake) + self._dateEmprunt):^15}|\n"
        return s

    def isLate(self) -> bool:
        """
        Vérifie si l'Emprunt est en retard
        :return:
        """
        return (date.today() - self._dateEmprunt).days >= self._nbDayMake

    def empruntTerminate(self) -> 'Document':
        """
        Rend le document via la fonction giveBack
        :return:
        """
        self._doc.giveBack()
        return self._doc

    def getDoc(self) -> str:
        """
        Return le document
        :return:
        """
        return self._doc.getEmprunt()


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

    def __str__(self):
        s = f"Adhérent: {self._name}\n"
        s += '/----------------------------------------------------------------------------------------------------------------------\ \n'
        s += f"|{'index':^6}|{'Document':^10}|{'titre': ^26}|{'auteur/compositeur': ^20}|{'Interprete':20}|{'Depuis le':^15}|{'Retour le':^15}| \n"
        s += '|----------------------------------------------------------------------------------------------------------------------|\n'
        for index, d in enumerate(self._borrowingInProgress):
            s += f"|{index:^6}|{str(d)}"
        s += "\----------------------------------------------------------------------------------------------------------------------/"
        return s

    def isLate(self) -> bool:
        """
        Vérifie si le document est
        en retard
        :return:
        """
        for emprunt in self._borrowingInProgress:
            if emprunt.isLate():
                return True
        return False

    def borrowingTrue(self) -> bool:
        """
        Vérifie si l'Adhérent n'a pas plus de
        5 documents
        :return:
        """
        return len(self._borrowingInProgress) < 5

    def emprunter(self, doc: Document):
        """
        Méthode permettant d'emprunter
        un document présent dans la médiathèque
        :param doc:
        :return:
        """
        if self.borrowingTrue() is True and not self.isLate():
            self._borrowingInProgress.append(doc.emprunter())
            doc.setEmprunt()
        else:
            print("[!] Ce livre est déjà emprunté")


    def terminer_emprunt(self, index: int):
        try:
            self._borrowingInProgress[index].empruntTerminate()
            self._borrowingInProgress.pop(index)
        except:
            return False

def main():



    m = Mediatheque()
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
    pierre.emprunter(m.getDocument(1))
    pierre.emprunter(m.getDocument(2))
    pierre.emprunter(m.getDocument(3))
    pierre.emprunter(m.getDocument(4))
    pierre.emprunter(m.getDocument(7))
    print(pierre)
    print('\n\n\n\n\n\n\n')
    pierre.terminer_emprunt(0)
    print(pierre)
    print(m)


if __name__ == '__main__':
    main()
