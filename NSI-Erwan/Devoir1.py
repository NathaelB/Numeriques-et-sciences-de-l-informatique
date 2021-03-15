from typing import List

def nb_car(chaine: str) -> int:
    count = len(chaine)
    print(int(count))


def moyenne_des_pairs(nombres: List[int]) -> float:
    moyenne = 0
    tab = []
    for i in nombres:
        if i % 2 == 0:
            moyenne += i
            tab.append(i)
    print(tab)
    return moyenne / len(tab)

if __name__ == '__main__':
    nb_car("J'aime les Mr.Freeze")
    print(moyenne_des_pairs([4, 5, 8, 7, 9, 12, 1]))
