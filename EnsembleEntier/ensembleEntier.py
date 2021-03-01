from multipledispatch import dispatch
from typing import List


class EE:
    @dispatch(int)
    def __init__(self, lmax:int):
        self.lmax = lmax
        self._cardinal = 0
        self.ens_tab = [None for _ in range(self.lmax)]

    @dispatch(int,list)
    def __init__(self,lmax:int,ensemble:List[int]):
        self.__init__(lmax)
        for i in range (len(ensemble)):
            if ensemble[i] not in self.ens_tab:
                self.ens_tab[self._cardinal]=ensemble[i]
                self._cardinal += 1

    @dispatch(list)
    def __init__(self,ensemble: 'EE'):
        self.lmax = ensemble.lmax
        self._cardinal = ensemble._cardinal
        self.ens_tab = [e for e in ensemble.ens_tab]


    @dispatch(object)
    def __init__(self, ensemble: 'EE'):
        self.ens_tab  = [i for i in ensemble.ens_tab]
        self.lmax  = ensemble.lmax
        self.cardinal  = ensemble.cardinal

    @dispatch(int, list, str)
    def __init__(self, lmax: int, ensemble: str):
        self.__init__(lmax, [int(e) for e in ensemble.split(" ")])

    def __str__(self) -> str:
        s = "{"
        for i in range(self._cardinal):
            s += str(self.ens_tab[i]) + ","
        if len(s) > 1 : s=s[:-1]
        return "================\n" + s + "}\n================"

    def getCardinal(self):
        return self._cardinal
        # for i in range(len(self.ens_tab)):
        #     cardinal += 1
        # return cardinal

    def contient_pratique(self, element: int) -> int:
        # try:
        #     return self.ens_tab.index(element)
        # except:
        #     return -1
        for i in range(self._cardinal):
            if self.ens_tab == element:
                return i
        return -1

    def contient(self, element:int) -> bool:
        """
        Fracturation du code, en repêchant la méthode de contient_pratique
        En vérifiant avec une condition ternaire, si l'élement de contient_pratique est différent de 1
        en renvoyant un boolean.
        :param element: Int
        :return: Bool
        """
        return self.contient_pratique(element) != -1

    def est_vide(self) -> bool:
        return self._cardinal == 0

    def _add(self, element: int):
        self.ens_tab[self._cardinal]= element
        self._cardinal += 1

    def _remove(self, index:int):
        for i in range(index, self._cardinal):
            self.ens_tab[i] = self.ens_tab[i + 1]
        self._cardinal -= 1

    def deborde(self) -> bool:
        return self._cardinal == self.lmax

    def retraitElt(self, element: int) -> bool:
        index = self.contient_pratique(element)
        if index > -1:
            self._remove(index)
            return True
        return False

    def ajoutElt(self, element:int) -> int:
        """
        Permet d'ajouter un élement

        :param element: int
        :return: int
        """
        if type(element) != int: return -1 # Opération ternaire
        index = self.contient_pratique(element)
        if index > -1: return 0
        if self.deborde(): return 0
        self._add(element)
        return 1

    def estInclu(self, ensemble: 'EE') -> bool:
        for i in self.ens_tab:
            if not ensemble.contient(i): return False
        return False


    def intersection(self, ensemble: 'EE') -> 'EE':
        inter = EE(self.lmax)
        for i in self.ens_tab:
            if ensemble.contient(i):
                inter.ajoutElt(i)
        return inter

    def reunion(self, ensemble: 'EE') -> 'EE':
        """

        :param ensemble: object<EE>
        :return: object<EE>
        """
        reunion = EE(self.getCardinal() + ensemble.getCardinal() - self.intersection(ensemble).getCardinal())
        for i in self.ens_tab :
            reunion.ajoutElt(i)
        for i in ensemble.ens_tab:
            reunion.ajoutElt(i)

    def difference(self, ensemble: 'EE') -> 'EE':
        """

        :param ensemble: object<EE>
        :return: object<EE>
        """
        diff = EE(self)
        inter = self.intersection(ensemble)
        for i in inter:
            diff.retraitElt(i)
        return diff


    #
    # def add_element(self,element:int):
    #     if element not in self.ens_tab:
    #         self.ens_tab[self.cardinal] = element
    #         self.cardinal += 1
    #     return element



def main():
    ee1 = EE(50)
    ee2 = EE(50, [8, 7, 6, 8])
    print(ee1)
    print(ee2)
    print(ee1.getCardinal())
    print(ee1.reunion(ee2))
    print(ee1.difference(ee2))

if __name__ == '__main__':
    main()
