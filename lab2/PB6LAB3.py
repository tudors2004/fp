def cea_mai_lunga_subsecventa_domino(lista):
    cea_mai_lunga_subsecventa = []
    subsecventa_curenta = [lista[0]]

    for i in range(1, len(lista)):
        if lista[i][0] == lista[i - 1][1]:
            subsecventa_curenta.append(lista[i])
        else:
            subsecventa_curenta = [lista[i]]

        if len(subsecventa_curenta) > len(cea_mai_lunga_subsecventa):
            cea_mai_lunga_subsecventa = subsecventa_curenta

    return cea_mai_lunga_subsecventa


def main():

    numere = ["89", "95", "54", "12", "23", "34", "45", "56", "21", "32"]

    print("Cea mai lunga subsecvența de domino:", cea_mai_lunga_subsecventa_domino(numere))


if __name__ == "__main__":
    main()
