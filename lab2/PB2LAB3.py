def nr_perechi_simetrice(lista):
    perechi_simetrice = set()

    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            if lista[i][::-1] == lista[j]:
                perechi_simetrice.add((lista[i], lista[j]))

    return len(perechi_simetrice)


def main():
    numere = ["56", "65", "69", "96", "89", "98", "12"]

    print("Nr perechi simetrice:", nr_perechi_simetrice(numere))


if __name__ == "__main__":
    main()
