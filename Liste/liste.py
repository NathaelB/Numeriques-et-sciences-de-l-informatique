from typing import Union,TypeVar,Any
Liste = TypeVar('Liste')

class Liste:
    def __init__(self, val: Union[Liste, Any] = None, queue: Liste = None):
        """Instancie  un objet Liste """
        if type(val) == Liste:
            self.tete = val.tete
            self.queue = val.queue
        else:
            self.tete = val
            self.queue = queue

    def __str__(self):
        """Retourne une chaîne de caractères des éléments de la Liste
        au format list python"""
        s = "["
        tete = self.tete
        queue = self.queue
        while tete is not None:
            s += str(tete) + ","
            if queue is None:
                break
            tete = queue.tete
            queue = queue.queue
        s = s[0: -1]
        s += "]"
        return s

    def __len__(self):
        """Retourne le nombre d'élément de la liste"""
        if self.tete is None:
            return 0
        elif self.queue is None:
            return 1
        else:
            return 1 + self.queue.__len__()

    def isEmpty(self):
        """ Retourne True si la liste est vide et False dans le cas contraire"""
        return self.tete is None

    def addHead(self, valeur):
        """ajoute une <valeur> en début de liste"""
        l = Liste(valeur)
        l.queue = Liste(self)
        self.tete, self.queue = l.tete, l.queue

    def deleteHead(self):
        """supprime une <valeur> en fin de liste"""
        self.tete = self.queue.tete
        self.queue = self.queue.queue

    def addQueue(self, val):
        """ajoute une <valeur> en fin de liste"""
        if self.tete is None:  # Si tete = none alors on lui ajoute la valeur de tete = val
            self.tete = val
        elif self.queue is None:  # Si tete = val et que queue = none alors self.queue = Liste(Val)
            self.queue = Liste(val)
        else:
            queue = self.queue
            while type(queue) is Liste:
                if queue.queue is None:
                    queue.queue = Liste(val)  # On ajoute ici la valeur Liste(val) dans la queue de queue
                    break
                queue = queue.queue


def main():
    liste1 = Liste()
    print(liste1)

if __name__ == '__main__':
    main()
