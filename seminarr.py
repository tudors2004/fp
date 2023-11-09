import random

numarul = input("pune un nr : ")
if numarul.isdigit():
    numarul = int(numarul)
    if numarul <= 0:
        print("pune nr mai mare egal cu 0")
        quit()
else:
    print("scrie un nr")
    quit()

numar_random = random.randint(0, numarul)
incercari = 0

while True:
 incercari += 1
 user = input("ghiceste numarul:")
 if user.isdigit():
        user = int(user)
 else:
        print("nu i bun scrie un numar")
        continue

 if user == numar_random:
            print("bravo")
            break
 elif user > numar_random:
            print ("numaru e mai mic")
 else:
            print("numaru e mai mare")

print("ai nimerit o din ", incercari, "incercari")
