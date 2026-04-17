def kresli(pocet, znak):
    # Funkcia využíva cyklus na opakované vykonanie príkazu.
    # Počet opakovaní je riadený hodnotou premennej pocet.

    vystup = ""

    # Cyklus for zabezpečuje opakovanie činnosti daný počet krát
    # V každom kroku cyklu sa pridá jeden znak do výstupu

    for i in range(pocet):
        vystup = vystup + znak

    # Výsledkom je riadok znakov. 
    print(vystup)

    # Textová informácia o výsledku
    print("Vytvoril som", pocet, "prvkov.")


def main():
    pocet = int(input("Zadaj počet prvkov: "))

    # Používateľ si zvolí znak, ktorý nahrádza grafický objekt
    znak = input("Zadaj znak: . , *, #, pismeno, cislo: ")

    kresli(pocet, znak)


main()
