def cel_mai_mare_numar(lista):
    return ''.join(sorted(lista, key=lambda x: x + x[::-1], reverse=True))


def main():
    numere = ["41", "14", "97", "55"]

    print("Cel mai mare numar posibil:", cel_mai_mare_numar(numere))


if __name__ == "__main__":
    main()
