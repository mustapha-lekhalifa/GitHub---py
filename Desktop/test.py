import random

def main():
    print("Bienvenue dans le jeu de football !")
    jouer()

def jouer():
    joueur1 = input("Entrez le nom du joueur 1 : ")
    joueur2 = input("Entrez le nom du joueur 2 : ")

    score_joueur1 = 0
    score_joueur2 = 0
    tour = 1

    while tour <= 5:
        print(f"\nTour {tour} :")
        input(f"Appuyez sur Entrée pour que {joueur1} tire...")
        but1 = random.randint(0, 1)
        score_joueur1 += but1
        print(f"{joueur1} a marqué {but1} but(s) ! Score total : {score_joueur1}")

        input(f"Appuyez sur Entrée pour que {joueur2} tire...")
        but2 = random.randint(0, 1)
        score_joueur2 += but2
        print(f"{joueur2} a marqué {but2} but(s) ! Score total : {score_joueur2}")

        tour += 1

    print("\nLe match est terminé ! Voici le résultat final :")
    print(f"{joueur1} : {score_joueur1} but(s)")
    print(f"{joueur2} : {score_joueur2} but(s)")

    if score_joueur1 > score_joueur2:
        print(f"{joueur1} remporte la victoire !")
    elif score_joueur2 > score_joueur1:
        print(f"{joueur2} remporte la victoire !")
    else:
        print("Match nul !")

if __name__ == "__main__":
    main()


