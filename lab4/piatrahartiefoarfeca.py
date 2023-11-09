import random
scor_jucator = 0
scor_calculator = 0
optiuni = ['piatra', 'foarfeca', 'hartie']
while True:
    jucator = input("Alege Piatra/Hartie/Foarfeca: ").lower()
    if jucator not in optiuni:
        break

    numar = random.randint(0, 2)
     # piatra = 0 hartie = 1 foarfeca = 2
    calculator = optiuni[numar]
    print("Calculatorul alege: ", calculator)

    if jucator == 'hartie' and calculator == 'piatra':
        print("Ai castigat!")
        scor_jucator += 1
    elif jucator == 'foarfeca' and calculator == 'hartie':
        print("Ai castigat!")
        scor_jucator += 1
    elif jucator == 'piatra' and calculator == 'foarfeca':
        print("Ai castigat!")
        scor_jucator += 1
    elif jucator == calculator:
        print("Egalitate")

    else:
        print("Ai pierdut! Mai incearca..")
        scor_calculator += 1


print("Scorul calculatorului este: ", scor_calculator)
print("Scorul jucatorului este: ", scor_jucator)

print("Pa")
