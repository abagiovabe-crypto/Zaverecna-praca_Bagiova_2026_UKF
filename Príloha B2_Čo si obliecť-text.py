def rozhodni(pocasie):
    # Funkcia spracúva vstup a na jeho základe riadi správanie programu.

    # Podmienené vetvenie – program vyberá jednu z možností podľa hodnoty premennej.
    if pocasie == "slnečno":
        print("Zober si tričko.")
        # Program vykonáva viac výstupov v jednej vetve

    elif pocasie == "dážď":
        print("Zober si dáždnik.")

    elif pocasie == "sneh":
        print("Zober si bundu.")

    else:
        # Vetva sa vykoná, ak žiadna z podmienok neplatí
        print("Neznáme počasie.")
        print("Zadaj: slnečno, dážď alebo sneh.")


def main():
    # Hlavná funkcia riadi tok programu a zabezpečuje prepojenie vstupu a spracovania.

    pocasie = input("Zadaj počasie: ")

    # Zavolanie funkcie, ktorá realizuje rozhodovanie
    rozhodni(pocasie)


main()
