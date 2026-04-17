def kresli(pocet):
    # Funkcia využíva cyklus while, ktorý sa opakuje,
    # pokiaľ nie je splnená podmienka na jeho ukončenie.

    i = 0  # počítadlo iterácií

    while True:
        # Cyklus je s neurčitým počtom opakovaní (while True),
        # preto je potrebné ho ukončiť pomocou break.

        if i >= pocet:
            break

        # V každom kroku cyklu sa vykoná jedna akcia
        print("o", end="")

        # Zvýšenie počítadla – posun na ďalšiu iteráciu
        i = i + 1

    # Po skončení cyklu prechod na nový riadok
    print()


def main():
    pocet = int(input("Zadaj počet bodov: "))

    # Zavolanie funkcie
    kresli(pocet)


main()
