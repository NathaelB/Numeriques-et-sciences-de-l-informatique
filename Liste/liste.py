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

def main():
    liste1 = Liste()
    print(liste1)

if __name__ == '__main__':
    main()
