import random

nombre = random.randint(1, 100)
question = "Devine le nombre : "
essais = 5

print("*** Le jeu du nombre mystère ***")

while essais != 0:
    print(f"Il te reste {essais} essais")
    reponse = input(question)

    if not reponse.isdigit():
        print("Veuillez entrez un nombre valide.")
        continue

    if int(reponse) > nombre:
        print(f"Le nombre mystère est plus petit que {reponse}")
        essais -= 1
    elif int(reponse) < nombre:
        print(f"Le nombre mystère est plus grand que {reponse}")
        essais -= 1
    elif int(reponse) == nombre:
        print(f"Bravo, le nombre mystère était bien {reponse} !")
        print(f"Vous avez eu besoin de {essais} essais pour trouver la bonne réponse")
        break

    if essais == 0:
        print(f"Dommage ! le nombre mystère était {nombre}")

print("Fin du jeu.")