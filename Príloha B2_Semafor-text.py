def rozhodni(farba):
    # Funkcia prijíma vstup od používateľa (premennú farba).
    # Na základe hodnoty vstupu rozhoduje o tom, aký výstup program zobrazí.

    # Podmienené príkazy riadia tok programu podľa zadaného textu.
    if farba == "červená":
        print("Stoj")
    elif farba == "oranžová":
        print("Priprav sa")
    elif farba == "zelená":
        print("Choď")
    else:
        # Vetva, ktorá sa vykoná, ak neplatí žiadna z uvedených podmienok.
        print("Neznáma farba")


def main():
    # Hlavná funkcia programu zabezpečuje jeho riadenie.

    print("Semafor slov")
    farba = input("Zadaj farbu semaforu: ")

    # Zavolanie funkcie, ktorá spracuje vstup a rozhodne o výstupe.
    rozhodni(farba)


# Spustenie programu
main()
