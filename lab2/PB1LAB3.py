def elimina_duplicate(lista):
    return list(set(lista))


def main():
    numere = ["12", "34", "56", "12", "78", "34", "90"]

    print("Lista fara duplicate:", elimina_duplicate(numere))


if __name__ == "__main__":
    main()
