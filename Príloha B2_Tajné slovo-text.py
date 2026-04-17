def skontroluj(slovo):
    # Funkcia prijíma vstup od používateľa (premennú slovo).
    # Jej úlohou je vyhodnotiť zadanú hodnotu a rozhodnúť o výstupe programu.

    # Podmienený príkaz porovnáva hodnotu premennej so zadaným textom.
    
    if slovo == "slnko":
        print("Správne tajné slovo")
    else:
        print("Skús znova")


def main():
    # Hlavná funkcia programu riadi jeho priebeh.
    # Obsahuje vstup, spracovanie aj výstup.

    print("Tajné slovo")
    slovo = input("Zadaj tajné slovo: ")

    # Zavolanie funkcie, ktorá spracuje vstup a rozhodne o výsledku.
    skontroluj(slovo)


# Spustenie programu
main()
