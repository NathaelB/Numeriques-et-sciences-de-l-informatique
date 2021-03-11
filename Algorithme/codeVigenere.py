
def polynome(x: float, coefficient: list):
    return sum([x ** i * c for i, c in enumerate(coefficient)])


def selectionSorting(list):
    for i in range(len(list)):
        mini = i
        for j in range(i, len(list)):
            if list[j] < list[mini]:
                mini = j
        list[i], list[mini] = list[mini], list[i]
    return list


def main():
    print(polynome(7.2, [7, 15, 2]))


if __name__ == '__main__':
    main()
