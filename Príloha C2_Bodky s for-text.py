def kresli(pocet):
    # Funkcia riadi opakované vykonanie činnosti pomocou cyklu.
    # Počet opakovaní je daný hodnotou premennej pocet.

    # Cyklus for zabezpečuje, že sa príkaz vykoná presne pocet-krát
    for i in range(pocet):
        print("o", end="")

    # Po skončení cyklu sa prejde na nový riadok
    print()


def main():
    pocet = int(input("Zadaj počet bodov: "))

    # Zavolanie funkcie, ktorá realizuje opakovanie
    kresli(pocet)


main()
