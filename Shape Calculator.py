import math

#Functions to simplify math
Pi = math.pi
Q = (4/3)
Qa = (4 / (3 ** 0.5))
Qb = (1/4)
Qc = (1/2)
Qd = (1/3)
sqrt = math.sqrt


#Efface la console
def clear():
    print("\n" * 50 )

#ENGLAIS
#Function pour la calcule d'un cercle
def circleen():
    try:
        R = int(input("What is the Radius of the circle: "))
        Area = ((Pi * R) ** 2)
        Peri = (2 * (Pi * R))
        print(f"Area: {Area.__round__(2)}\n"
              f"Perimeter: {Peri.__round__(2)}")
        input("Press enter to continue!\n")
    except ValueError:
        print("Incorrect, Try again")
        input("Press enter to continue!\n")

#Function pour la calcule d'un Sphere
def sphereen():
    try:
        R = int(input("What is the Radius of the Sphere: "))
        Area = (4 * ((Pi * R) ** 2))
        Volu = ((Q * Pi * R) ** 3)
        print(f"Area: {Area.__round__(2)}\n"
              f"Volume: {Volu.__round__(2)}")
        input("Press enter to continue")
    except ValueError:
        print("Incorrect, Try again")
        input("Press enter to continue!\n")

#Function pour la calcule d'un Square
def squareen():
    try:
        Length = int(input("What is the Length of the base: "))
        Width = int(input("What is the Width of the base: "))
        Peri = (Length * 2) + (Width * 2)
        Area = (Length * Width)
        print(f"Perimeter: {Peri.__round__(2)}\n"
              f"Area: {Area.__round__(2)}")
        input("Press enter to continue!\n")
    except ValueError:
        print("Incorrect, Try again")
        input("Press enter to continue!\n")

#Function pour la calcule d'un Cube
def cubeen():
    try:
        Length = int(input("What is the Length of the base: "))
        Width = int(input("What is the Width of the base: "))
        Height = int(input("What is the Height of the Cube: "))
        Volu = Length * Width * Height
        Area = 2 * (Length + Width + Height)
        print(f"Area: {Area.__round__(2)}\n"
              f"Volume: {Volu.__round__(2)}")
        input("Press enter to continue!\n")
    except ValueError:
        print("Incorrect, Try again")
        input("Press enter to continue!\n")

#Function pour la calcule d'un Triangle
def triangleen():
    try:
        print("Options:\n 1. Equilateral\n 2. Isosceles\n 3. Scalene")
        Type = int(input("What type of triangle is it: "))
        if Type == 1:
            try:
                A = int(input("What is the Length of 1 side: "))
                Peri = (3 * A)
                Area = ((Qa * A) ** 2)
                print(f"Perimeter: {Peri.__round__(2)}\n"
                      f"Area: {Area.__round__(2)}")
                input("Press enter to continue!\n")
            except ValueError:
                print("Incorrect, Try again")
                input("Press enter to continue!\n")
        elif Type == 2:
            try:
                A = int(input("what is the A sides of the triangle: "))
                B = int(input("What is the B side of the triangle: "))
                Peri = (2 * A) + B
                Area = (Qb * B) * (((4 * A) ** 2) - (B ** 2) ** 0.5)
                print(f"Perimeter: {Peri.__round__(2)}\n"
                      f"Area: {Area.__round__(2)}")
                input("Press enter to continue!\n")
            except ValueError:
                print("Incorrect, Try again")
                input("Press enter to continue!\n")
        elif Type == 3:
            try:
                A = int(input("what is the A side of the triangle: "))
                B = int(input("What is the B side of the triangle: "))
                C = int(input("What is the C side of the triangle: "))
                Peri = A + B + C
                S = Peri / 2
                Area = (S * (S - A) * (S - B) * (S - C)) ** 0.5
                print(f"Perimeter: {Peri.__round__(2)}\n"
                      f"Semi Perimeter: {S.__round__(2)}\n"
                      f"Area: {Area.__round__(2)}")
                input("Press enter to continue!\n")
            except ValueError:
                print("Incorrect, Try again")
                input("Press enter to continue!\n")
    except ValueError:
        print("Incorrect, Try again")
        input("Press enter to continue!\n")

#Function pour la calcule d'un Pyramid
def pyramiden():
    Length = int(input("What is the Length of the triangle: "))
    Height = int(input("What is the Height of the triangle:"))
    Base = Length ** 2
    Volu = Qd * Base * Height
    print(f"Volume: {Volu.__round__(2)}")
    input("Press enter to continue!\n")

#Function pour la calcule d'un Hypotenuse
def hypotenuseen():
    try:
        print("[1] Find A. [2] Find B. [3] Find C.")
        missing = input("What side is missing?\n>")
        if missing == "1":
            try:
                SideB = int(input("What is the length of Side B\n>"))
                SideC = int(input("What is the length of Side C\n>"))
                A = ((SideC ** 2) - (SideB ** 2)) ** 0.5
                print(f"The value of A is {A}")
                input("Press enter to continue!\n")
            except ValueError:
                print("Faux. Essayez à nouveau")
                input("Appuyez sur Entrée pour continuer!\n")
        if missing == "2":
            try:
                SideA = int(input("What is the length of Side A\n>"))
                SideC = int(input("What is the length of Side C\n>"))
                B = ((SideC ** 2) - (SideA ** 2)) ** 0.5
                print(f"The value of B is {B}")
                input("Press enter to continue!\n")
            except ValueError:
                print("Faux. Essayez à nouveau")
                input("Appuyez sur Entrée pour continuer!\n")
        if missing == "3":
            try:
                SideA = int(input("What is the length of Side A\n>"))
                SideB = int(input("What is the length of Side B\n>"))
                C = ((SideA ** 2) + (SideB ** 2)) ** 0.5
                print(f"The value of C is {C}")
                input("Press enter to continue!\n")
            except ValueError:
                print("Faux. Essayez à nouveau")
                input("Appuyez sur Entrée pour continuer!\n")
    except ValueError:
        print("Faux. Essayez à nouveau")
        input("Appuyez sur Entrée pour continuer!\n")



#FRANCAIS
# Function pour la calcule d'un cercle
def circlefr():
    try:
        R = int(input("Quel est le rayon du cercle: "))
        Area = ((Pi * R) ** 2)
        Peri = (2 * (Pi * R))
        print(f"Aire: {Area.__round__(2)}\n"
              f"Périmètre: {Peri.__round__(2)}")
        input("Appuyez sur Entrée pour continuer!\n")
    except ValueError:
        print("Faux. Essayez à nouveau")
        input("Appuyez sur Entrée pour continuer!\n")

# Function pour la calcule d'un Sphere
def spherefr():
    try:
        R = int(input("Quel est le rayon du Sphere: "))
        Area = (4 * ((Pi * R) ** 2))
        Volu = ((Q * Pi * R) ** 3)
        print(f"Aire: {Area.__round__(2)}\n"
              f"Périmètre: {Volu.__round__(2)}")
        input("Appuyez sur Entrée pour continuer")
    except ValueError:
        print("Faux. Essayez à nouveau")
        input("Appuyez sur Entrée pour continuer!\n")

# Function pour la calcule d'un Square
def squarefr():
    try:
        Length = int(input("Quelle est la longueur de la base: "))
        Width = int(input("Quelle est la largeur de la base: "))
        Peri = (Length * 2) + (Width * 2)
        Area = (Length * Width)
        print(f"Périmètre: {Peri.__round__(2)}\n"
              f"Aire: {Area.__round__(2)}")
        input("Appuyez sur Entrée pour continuer")
    except ValueError:
        print("Faux. Essayez à nouveau")
        input("Appuyez sur Entrée pour continuer!\n")

# Function pour la calcule d'un Cube
def cubefr():
    try:
        Length = int(input("Quelle est la longueur de la base: "))
        Width = int(input("Quelle est la largeur de la base: "))
        Height = int(input("Quelle est la hauteur du cube: "))
        Volu = Length * Width * Height
        Area = 2 * (Length + Width + Height)
        print(f"Aire: {Area.__round__(2)}\n"
              f"Volume: {Volu.__round__(2)}")
        input("Appuyez sur Entrée pour continuer")
    except ValueError:
        print("Faux. Essayez à nouveau")
        input("Appuyez sur Entrée pour continuer!\n")

# Function pour la calcule d'un Triangle
def trianglefr():
    try:
        print("Choix:\n 1. Équilatéral\n 2. Isocèle\n 3. Scalène")
        Type = int(input("De quel type de triangle s'agit-il: "))
        if Type == 1:
            try:
                A = int(input("Quelle est la longueur d'un côté: "))
                Peri = (3 * A)
                Area = ((Qa * A) ** 2)
                print(f"Périmètre: {Peri.__round__(2)}\n"
                      f"Aire: {Area.__round__(2)}")
                input("Appuyez sur Entrée pour continuer")
            except ValueError:
                print("Faux. Essayez à nouveau")
                input("Appuyez sur Entrée pour continuer!\n")
        elif Type == 2:
            try:
                A = int(input("Quel est le côté A du triangle: "))
                B = int(input("Quel est le côté B du triangle: "))
                Peri = (2 * A) + B
                Area = (Qb * B) * (((4 * A) ** 2) - (B ** 2) ** 0.5)
                print(f"Perimeter: {Peri.__round__(2)}\n"
                      f"Area: {Area.__round__(2)}")
                input("Appuyez sur Entrée pour continuer")
            except ValueError:
                print("Faux. Essayez à nouveau")
                input("Appuyez sur Entrée pour continuer!\n")
        elif Type == 3:
            try:
                A = int(input("Quel est le côté A du triangle: "))
                B = int(input("Quel est le côté B du triangle: "))
                C = int(input("Quel est le côté C du triangle: "))
                Peri = A + B + C
                S = Peri / 2
                Area = (S * (S - A) * (S - B) * (S - C)) ** 0.5
                print(f"Perimeter: {Peri.__round__(2)}\n"
                      f"Semi Perimeter: {S.__round__(2)}\n"
                      f"Area: {Area.__round__(2)}")
                input("Appuyez sur Entrée pour continuer")
            except ValueError:
                print("Faux. Essayez à nouveau")
                input("Appuyez sur Entrée pour continuer!\n")
    except ValueError:
        print("Faux. Essayez à nouveau")
        input("Appuyez sur Entrée pour continuer!\n")

# Function pour la calcule d'un Pyramid
def pyramidfr():
    try:
        Length = int(input("Quelle est la longueur du triangle: "))
        Height = int(input("Quelle est la hauteur du triangle: "))
        Base = Length ** 2
        Volu = Qd * Base * Height
        print(f"Volume: {Volu.__round__(2)}")
        input("Appuyez sur Entrée pour continuer")
    except ValueError:
        print("Faux. Essayez à nouveau")
        input("Appuyez sur Entrée pour continuer!\n")

# Fonction de calcul d'une Hypoténuse
def hypotenusefr():
    try:
        print("[1] Trouver A. [2] Trouver B. [3] Trouver C.")
        missing = input("Quel côté manque?\n>")
        if missing == "1":
            try:
                SideB = int(input("Quelle est la longueur du côté B\n>"))
                SideC = int(input("Quelle est la longueur du côté C\n>"))
                A = ((SideC ** 2) - (SideB ** 2)) ** 0.5
                print(f"La valeur de A est {A}")
                input("Appuyez sur Entrée pour continuer")
            except ValueError:
                print("Faux. Essayez à nouveau")
                input("Appuyez sur Entrée pour continuer!\n")
        if missing == "2":
            try:
                SideA = int(input("Quelle est la longueur du côté A\n>"))
                SideC = int(input("Quelle est la longueur du côté C\n>"))
                B = ((SideC ** 2) - (SideA ** 2)) ** 0.5
                print(f"La valeur de B est {B}")
                input("Appuyez sur Entrée pour continuer")
            except ValueError:
                print("Faux. Essayez à nouveau")
                input("Appuyez sur Entrée pour continuer!\n")
        if missing == "3":
            try:
                SideA = int(input("Quelle est la longueur du côté A\n>"))
                SideB = int(input("Quelle est la longueur du côté B\n>"))
                C = ((SideA ** 2) + (SideB ** 2)) ** 0.5
                print(f"La valeur de C est {C}")
                input("Appuyez sur Entrée pour continuer")
            except ValueError:
                print("Faux. Essayez à nouveau")
                input("Appuyez sur Entrée pour continuer!\n")
    except ValueError:
        print("Faux. Essayez à nouveau")
        input("Appuyez sur Entrée pour continuer!\n")

#Choix de language
lang = int(input("What Language will you be using?   [1] English\n"
                 "Quelle langue allez-vous utiliser? [2] Francais\n"
                 ">"))

#La System Anglais
if lang == 1:
    SYSEN = True
    cir = True
    while SYSEN:
        clear()
        try:
            Shape = int(input("Options:\n 1. Circle\n 2. Sphere\n 3. Square\n 4. Cube\n 5. Triangle\n 6. Pyramid\n 7. Hypotenuse\n 8. Quit\n"
                              "What Shape are you using?\n>"))
            clear()
            if Shape == 1:
                circleen()
                clear()
            elif Shape == 2:
                clear()
                sphereen()
            elif Shape == 3:
                clear()
                squareen()
            elif Shape == 4:
                clear()
                cubeen()
            elif Shape == 5:
                clear()
                triangleen()
            elif Shape == 6:
                clear()
                pyramiden()
            elif Shape == 7:
                clear()
                hypotenuseen()
            elif Shape == 8:
                clear()
                SYSEN = False
        except ValueError:
            print("Incorrect, Try again")
            input("Press enter to continue!\n")

#La System Francais
elif lang == 2:
    SYSFR = True
    while SYSFR:
        clear()
        try:
            Shape = int(input("Choix:\n 1. Cercle\n 2. Sphère\n 3. Carré\n 4. Cube\n 5. Triangle\n 6. Pyramide\n 7. Hypoténuse\n 8. Arrêter\n"
                          "Quelle forme utilisez-vous?\n>"))
            clear()
            if Shape == 1:
                circlefr()
                clear()
            elif Shape == 2:
                clear()
                spherefr()
            elif Shape == 3:
                clear()
                squarefr()
            elif Shape == 4:
                clear()
                cubefr()
            elif Shape == 5:
                clear()
                trianglefr()
            elif Shape == 6:
                clear()
                pyramidfr()
            elif Shape == 7:
                clear()
                hypotenusefr()
            elif Shape == 8:
                clear()
                SYSFR = False
        except ValueError:
            print("Faux. Essayez à nouveau")
            input("Appuyez sur Entrée pour continuer!\n")

if lang == 1:
    print("Thanks for using the calculator")
elif lang == 2:
    print("Merci d'avoir utilisé la calculatrice")
